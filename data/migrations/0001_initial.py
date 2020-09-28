# Generated by Django 3.1.1 on 2020-09-27 17:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalystRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BulkPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('history', models.JSONField(blank=True, null=True)),
                ('trend', models.JSONField(blank=True, null=True)),
                ('annual', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ESGScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('rating_date', models.CharField(blank=True, max_length=50, null=True)),
                ('total_esg', models.FloatField(blank=True, null=True)),
                ('total_esg_percentile', models.FloatField(blank=True, null=True)),
                ('environment_score', models.FloatField(blank=True, null=True)),
                ('environment_score_percentile', models.FloatField(blank=True, null=True)),
                ('social_score', models.FloatField(blank=True, null=True)),
                ('social_score_percentile', models.FloatField(blank=True, null=True)),
                ('governance_score', models.FloatField(blank=True, null=True)),
                ('governance_score_percentile', models.FloatField(blank=True, null=True)),
                ('controversy_level', models.IntegerField(blank=True, null=True)),
                ('activities_involvement', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Financials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('financial_type', models.CharField(blank=True, max_length=50, null=True)),
                ('currency_symbol', models.CharField(blank=True, max_length=20, null=True)),
                ('period', models.CharField(blank=True, max_length=20, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('sec_type', models.CharField(blank=True, max_length=50, null=True)),
                ('exchange', models.CharField(blank=True, max_length=50, null=True)),
                ('currency_code', models.CharField(blank=True, max_length=50, null=True)),
                ('currency_name', models.CharField(blank=True, max_length=50, null=True)),
                ('currency_symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('country_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country_iso', models.CharField(blank=True, max_length=50, null=True)),
                ('isin', models.CharField(blank=True, max_length=50, null=True)),
                ('cusip', models.CharField(blank=True, max_length=50, null=True)),
                ('cik', models.CharField(blank=True, max_length=50, null=True)),
                ('employer_id_number', models.CharField(blank=True, max_length=50, null=True)),
                ('fiscal_year_end', models.CharField(blank=True, max_length=50, null=True)),
                ('ipo_date', models.CharField(blank=True, max_length=50, null=True)),
                ('international_domestic', models.CharField(blank=True, max_length=50, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('gic_sector', models.CharField(blank=True, max_length=100, null=True)),
                ('gic_group', models.CharField(blank=True, max_length=100, null=True)),
                ('gic_industry', models.CharField(blank=True, max_length=100, null=True)),
                ('gic_subindustry', models.CharField(blank=True, max_length=100, null=True)),
                ('home_category', models.CharField(blank=True, max_length=50, null=True)),
                ('is_delisted', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('listings', models.JSONField(blank=True, null=True)),
                ('officers', models.JSONField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('web_url', models.CharField(blank=True, max_length=50, null=True)),
                ('logo_url', models.CharField(blank=True, max_length=50, null=True)),
                ('fulltime_employee', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('market_capitalization', models.BigIntegerField(blank=True, null=True)),
                ('market_capitalization_mln', models.FloatField(blank=True, null=True)),
                ('ebitda', models.BigIntegerField(blank=True, null=True)),
                ('pe_ratio', models.FloatField(blank=True, null=True)),
                ('peg_ratio', models.FloatField(blank=True, null=True)),
                ('wallstreet_target_price', models.FloatField(blank=True, null=True)),
                ('book_value', models.FloatField(blank=True, null=True)),
                ('dividend_share', models.FloatField(blank=True, null=True)),
                ('dividend_yield', models.FloatField(blank=True, null=True)),
                ('earnings_share', models.FloatField(blank=True, null=True)),
                ('eps_estimate_current_year', models.FloatField(blank=True, null=True)),
                ('eps_estimate_next_year', models.FloatField(blank=True, null=True)),
                ('eps_estimate_next_quarter', models.FloatField(blank=True, null=True)),
                ('eps_estimate_current_quarter', models.FloatField(blank=True, null=True)),
                ('most_recent_quarter', models.CharField(blank=True, max_length=50, null=True)),
                ('profit_margin', models.FloatField(blank=True, null=True)),
                ('operating_margin_ttm', models.FloatField(blank=True, null=True)),
                ('roa_ttm', models.FloatField(blank=True, null=True)),
                ('roe_ttm', models.FloatField(blank=True, null=True)),
                ('revenue_ttm', models.BigIntegerField(blank=True, null=True)),
                ('revenue_per_share_ttm', models.FloatField(blank=True, null=True)),
                ('quarterly_revenue_growth_yoy', models.FloatField(blank=True, null=True)),
                ('gross_profit_ttm', models.BigIntegerField(blank=True, null=True)),
                ('diluted_eps_ttm', models.FloatField(blank=True, null=True)),
                ('quarterly_earnings_growth_yoy', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Holders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(blank=True, max_length=30, null=True)),
                ('price', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
                ('general', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
                ('highlights', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
                ('valuation', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
                ('shares_stats', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
                ('esg_scores', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
                ('earnings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
                ('financials', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='MetaDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('updated_date', models.CharField(blank=True, max_length=30, null=True)),
                ('tickers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('price', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('general', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('highlights', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('valuation', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('shares_stats', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('esg_scores', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('earnings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
                ('financials', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='OutstandingShares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('open_p', models.FloatField(blank=True, null=True)),
                ('high_p', models.FloatField(blank=True, null=True)),
                ('low_p', models.FloatField(blank=True, null=True)),
                ('close_p', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('volume', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SharesStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('shares_outstanding', models.BigIntegerField(blank=True, null=True)),
                ('shares_float', models.BigIntegerField(blank=True, null=True)),
                ('percent_insiders', models.FloatField(blank=True, null=True)),
                ('percent_institutions', models.FloatField(blank=True, null=True)),
                ('shares_short', models.BigIntegerField(blank=True, null=True)),
                ('shares_short_prior_month', models.BigIntegerField(blank=True, null=True)),
                ('short_ratio', models.FloatField(blank=True, null=True)),
                ('short_percent_outstanding', models.FloatField(blank=True, null=True)),
                ('short_percent_float', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SplitsDividends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Technicals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tickers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('tickers', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Valuation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('trailing_pe', models.FloatField(blank=True, null=True)),
                ('forward_pe', models.FloatField(blank=True, null=True)),
                ('price_sales_ttm', models.FloatField(blank=True, null=True)),
                ('price_book_mrq', models.FloatField(blank=True, null=True)),
                ('enterprise_value_revenue', models.FloatField(blank=True, null=True)),
                ('enterprise_value_ebitda', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
