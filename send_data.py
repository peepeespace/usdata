import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "usdata.settings")
application = get_wsgi_application()

from data.models import (
    MetaDate,
    MetaData,
    Tickers,
    Price,
    General,
    Highlights,
    Valuation,
    SharesStats,
    ESGScores,
    Earnings,
    Financials
)

from datetime import datetime
import redis
import requests
import pandas as pd
from dotenv import load_dotenv
from slacker import Slacker
from sensitives import SLACK_TOKEN

# Redis related functions
def cache_conn():
    redis_client = redis.Redis(host=cache_host, port=6379, password=cache_pw)
    return redis_client

def set_list(redis_client, data):
    response = redis_client.rpush(data[0], *data[1:])
    return response # returns 1 or 0

def get_list(redis_client, key, type='str'):
    response = redis_client.lrange(key, 0, -1)
    temp = response
    if type == 'int':
        try:
            is_int = int(response[0])
            response = list(map(lambda x: int(x), response))
        except ValueError:
            response = temp
    elif type == 'str':
        response = list(map(lambda x: x.decode('utf-8'), response))
    return response

def add_to_list(redis_client, key, data):
    response = redis_client.rpush(key, data)
    return response # returns 1 or 0

today = datetime.today().strftime('%Y%m%d')

cache_host = os.getenv('CACHE_HOST')
cache_pw = os.getenv('CACHE_PW')
api_token = os.getenv('API_TOKEN')

slack = Slacker(SLACK_TOKEN)
redis_client = cache_conn()

tickers_key = 'TICKERS_RECORD'
recent_date_key = 'RECENT_UPDATED_DATE'
price_key = 'PRICE_RECORD'
general_key = 'GENERAL_RECORD'
highlights_key = 'HIGHLIGHTS_RECORD'
valuation_key = 'VALUATION_RECORD'
sharesstats_key = 'SHARESSTATS_RECORD'
esgscores_key = 'ESGSCORES_RECORD'
earnings_key = 'EARNINGS_RECORD'
financials_key = 'FINANCIALS_RECORD'


# Slack related functions
def send_slack(task, msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        slack.chat.post_message('#general', f'({now}) [{task.upper()}]: {msg}')
    except:
        print(f'({now}) [{task.upper()}]: {msg}')


# Tasks
def save_tickers():
    ticker_list_api = f'https://eodhistoricaldata.com/api/exchange-symbol-list/US?fmt=json&api_token={api_token}'

    meta_exists = MetaDate.objects.filter(date=today).exists()
    data_exists = Tickers.objects.filter(date=today).exists()

    print(meta_exists)
    print(data_exists)
    if not meta_exists:
        print('meta does not exist')
        meta_date = MetaDate(date=today)
        if not data_exists:
            res = requests.get(ticker_list_api)
            print(res)
            json_data = res.json()
            t = Tickers(date=today, tickers=json_data)
            t.save()
            ticker_list = []
            meta_data_list = []
            for data in json_data:
                code = data['Code']
                ticker_list.append(code)
                if not MetaData.objects.filter(ticker=code).exists():
                    meta_data_list.append(MetaData(ticker=code))
            print(meta_date)
            meta_date.tickers = ticker_list
            meta_date.save()
            MetaData.objects.bulk_create(meta_data_list)
            send_slack('tickers', f'saved {today} tickers')
        else:
            t = Tickers.objects.filter(date=today)
            meta_date.tickers = t.tickers
            meta_date.save()
            meta_data_list = []
            tickers = t.tickers
            for code in tickers:
                if not MetaData.objects.filter(ticker=code).exists():
                    meta_data_list.append(MetaData(ticker=code))
            MetaData.objects.bulk_create(meta_data_list)
            send_slack('tickers', f'saved {today} tickers')
    else:
        send_slack('tickers', f'already saved {today} tickers')


def save_price():
    save_tickers()
    tickers = MetaData.objects.filter(date=today).tickers
    ticker_cnt = len(tickers)
    # send_slack('price', f'starting {today} price data save. Total tickers count: {ticker_cnt}')
    
    # if redis_client.exists(price_key):
    #     price_list = get_list(redis_client, price_key)
    #     if (price_list[0] != today):
    #         done_price_list = [price_key, today]
    #         set_list(redis_client, done_price_list)
    #     else:
    #         done_price_list = [price_key] + price_list
    # else:
    #     done_price_list = [price_key, today]
    #     set_list(redis_client, done_price_list)

    # cnt = 1
    # for ticker in tickers:
    #     if ticker not in done_price_list:
    #         existing_dates = [d.date for d in Price.objects.filter(code=ticker).all()]
    #         max_date = max(existing_dates) if len(existing_dates) != 0 else today

    #         if not redis_client.exists(recent_date_key):
    #             redis_client.set(recent_date_key, max_date)

    #         cached_recent_date = redis_client.get(recent_date_key).decode('utf-8')

    #         if (cnt == 1) or (cached_recent_date not in existing_dates):
    #             price_api = f'https://eodhistoricaldata.com/api/eod/{ticker}.US?fmt=json&api_token={api_token}'
    #             res = requests.get(price_api)
    #             res_json = res.json()
    #             data_points = []
    #             saved_dates = []
    #             for data in res_json:
    #                 if data['date'].replace('-', '') not in existing_dates:
    #                     p = Price(
    #                         code=ticker,
    #                         date=data['date'].replace('-', ''),
    #                         open_p=data['open'],
    #                         high_p=data['high'],
    #                         low_p=data['low'],
    #                         close_p=data['close'],
    #                         adj_close=data['adjusted_close'],
    #                         volume=data['volume']
    #                     )
    #                     data_points.append(p)
    #                     saved_dates.append(data['date'].replace('-', ''))
    #             Price.objects.bulk_create(data_points)
    #             redis_client.set(recent_date_key, max(saved_dates))
    #             done_price_list.append(ticker)
    #             redis_client.delete(price_key)
    #             set_list(redis_client, done_price_list)
    #             if cnt % 250 == 0:
    #                 send_slack('price', f'({cnt}/{ticker_cnt}) PRICE DATA DONE')
    #             print(f'({cnt}/{ticker_cnt}) {ticker} DONE')
    #             cnt += 1
    #         else:
    #             if cnt % 250 == 0:
    #                 send_slack('price', f'({cnt}/{ticker_cnt}) PRICE DATA DONE')
    #             print(f'({cnt}/{ticker_cnt}) {ticker} ALREADY DONE. SKIPPING...')
    #             cnt += 1
    #     else:
    #         if cnt % 250 == 0:
    #             send_slack('price', f'({cnt}/{ticker_cnt}) PRICE DATA DONE')
    #         print(f'({cnt}/{ticker_cnt}) {ticker} ALREADY DONE. SKIPPING...')
    #         cnt += 1

def save_financials():
    save_tickers()
    tickers = [d['Code'] for d in Tickers.objects.filter(date=today)[0].tickers]
    ticker = tickers[0]

    fundamental_api = f'https://eodhistoricaldata.com/api/fundamentals/{ticker}.US?fmt=json&api_token={api_token}'
    res = requests.get(fundamental_api)
    res_json = res.json()

    general = res_json['General']
    highlights = res_json['Highlights']
    valuation = res_json['Valuation']
    shares_stats = res_json['SharesStats']
    esg_scores = res_json['ESGScores']
    earnings = res_json['Earnings']
    financials = res_json['Financials']
    
    # General
    g = General(
        code=general['Code'],
        name=general['Name'],
        sec_type=general['Type'],
        exchange=general['Exchange'],
        currency_code=general['CurrencyCode'],
        currency_name=general['CurrencyName'],
        currency_symbol=general['CurrencySymbol'],
        country_name=general['CountryName'],
        country_iso=general['CountryISO'],
        isin=general['ISIN'],
        cusip=general['CUSIP'],
        cik=general['CIK'],
        employer_id_number=general['EmployerIdNumber'],
        fiscal_year_end=general['FiscalYearEnd'],
        ipo_date=general['IPODate'],
        international_domestic=general['InternationalDomestic'],
        sector=general['Sector'],
        industry=general['Industry'],
        gic_sector=general['GicSector'],
        gic_group=general['GicGroup'],
        gic_industry=general['GicIndustry'],
        gic_subindustry=general['GicSubIndustry'],
        home_category=general['HomeCategory'],
        is_delisted=general['IsDelisted'],
        description=general['Description'],
        address=general['Address'],
        listings=general['Listings'],
        officers=general['Officers'],
        phone=general['Phone'],
        web_url=general['WebURL'],
        logo_url=general['LogoURL'],
        fulltime_employee=general['FullTimeEmployees'],
        updated_at=general['UpdatedAt']
    )
    g.save()

    # Highlights
    h = Highlights(
        code=ticker,
        market_capitalization=highlights['MarketCapitalization'],
        market_capitalization_mln=highlights['MarketCapitalizationMln'],
        ebitda=highlights['EBITDA'],
        pe_ratio=highlights['PERatio'],
        peg_ratio=highlights['PEGRatio'],
        wallstreet_target_price=highlights['WallStreetTargetPrice'],
        book_value=highlights['BookValue'],
        dividend_share=highlights['DividendShare'],
        dividend_yield=highlights['DividendYield'],
        earnings_share=highlights['EarningsShare'],
        eps_estimate_current_year=highlights['EPSEstimateCurrentYear'],
        eps_estimate_next_year=highlights['EPSEstimateNextYear'],
        eps_estimate_next_quarter=highlights['EPSEstimateNextQuarter'],
        eps_estimate_current_quarter=highlights['EPSEstimateCurrentQuarter'],
        most_recent_quarter=highlights['MostRecentQuarter'],
        profit_margin=highlights['ProfitMargin'],
        operating_margin_ttm=highlights['OperatingMarginTTM'],
        roa_ttm=highlights['ReturnOnAssetsTTM'],
        roe_ttm=highlights['ReturnOnEquityTTM'],
        revenue_ttm=highlights['RevenueTTM'],
        revenue_per_share_ttm=highlights['RevenuePerShareTTM'],
        quarterly_revenue_growth_yoy=highlights['QuarterlyRevenueGrowthYOY'],
        gross_profit_ttm=highlights['GrossProfitTTM'],
        diluted_eps_ttm=highlights['DilutedEpsTTM'],
        quarterly_earnings_growth_yoy=highlights['QuarterlyEarningsGrowthYOY']
    )
    h.save()


    # Valuation
    v = Valuation(
        code=ticker,
        trailing_pe=valuation['TrailingPE'],
        forward_pe=valuation['ForwardPE'],
        price_sales_ttm=valuation['PriceSalesTTM'],
        price_book_mrq=valuation['PriceBookMRQ'],
        enterprise_value_revenue=valuation['EnterpriseValueRevenue'],
        enterprise_value_ebitda=valuation['EnterpriseValueEbitda']
    )
    v.save()

    # SharesStats
    s = SharesStats(
        code=ticker,
        shares_outstanding=shares_stats['SharesOutstanding'],
        shares_float=shares_stats['SharesFloat'],
        percent_insiders=shares_stats['PercentInsiders'],
        percent_institutions=shares_stats['PercentInstitutions'],
        shares_short=shares_stats['SharesShort'],
        shares_short_prior_month=shares_stats['SharesShortPriorMonth'],
        short_ratio=shares_stats['ShortRatio'],
        short_percent_outstanding=shares_stats['ShortPercentOutstanding'],
        short_percent_float=shares_stats['ShortPercentFloat']
    )
    s.save()

    # ESGScores
    esg = ESGScores(
        code=ticker,
        rating_date=esg_scores['RatingDate'],
        total_esg=esg_scores['TotalEsg'],
        total_esg_percentile=esg_scores['TotalEsgPercentile'],
        environment_score=esg_scores['EnvironmentScore'],
        environment_score_percentile=esg_scores['EnvironmentScorePercentile'],
        social_score=esg_scores['SocialScore'],
        social_score_percentile=esg_scores['SocialScorePercentile'],
        governance_score=esg_scores['GovernanceScore'],
        governance_score_percentile=esg_scores['GovernanceScorePercentile'],
        controversy_level=esg_scores['ControversyLevel'],
        activities_involvement=esg_scores['ActivitiesInvolvement']
    )
    esg.save()

    # Earnings
    e = Earnings(
        code=ticker,
        history=earnings['History'],
        trend=earnings['Trend'],
        annual=earnings['Annual']
    )
    e.save()

    # Financials
    for key in financials.keys():
        f = Financials(
            code=ticker,
            date=today,
            financial_type=key,
            currency_symbol=financials[key]['currency_symbol'],
            period='quarterly',
            data=financials[key]['quarterly']
        )
        f.save()

        f2 = Financials(
            code=ticker,
            date=today,
            financial_type=key,
            currency_symbol=financials[key]['currency_symbol'],
            period='yearly',
            data=financials[key]['yearly']
        )
        f2.save()


if __name__ == "__main__":
    save_price()

