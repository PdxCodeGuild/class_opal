import csv
import os
from django.core.management.base import BaseCommand
from django.db import connection, transaction
from personalized_index.models import Stock


class Command(BaseCommand):
    help = 'Import stock data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The CSV file to import stock data from')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        float_fields = ['trailingEps', 'forwardPE',
                        'marketCap', 'dividendYield', 'trailingPE']

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            with transaction.atomic():
                for row in reader:
                    symbol = row['symbol'].strip()
                    sector = row['sector'].strip()
                    long_business_summary = row['longBusinessSummary'].strip()
                    country = row['country'].strip()
                    short_name = row['shortName'].strip()
                    trailing_eps = row['trailingEps'].strip()
                    forward_pe = row['forwardPE'].strip()
                    market_cap = row['marketCap'].strip()
                    dividend_yield = row['dividendYield'].strip()
                    trailing_pe = row['trailingPE'].strip()

                    for field in float_fields:
                        try:
                            if row[field] == '':
                                row[field] = None
                            else:
                                row[field] = float(row[field])
                        except ValueError:
                            row[field] = None

                    stock = Stock(symbol=symbol, sector=sector, long_business_summary=long_business_summary,
                                  country=country, short_name=short_name, trailing_eps=trailing_eps,
                                  forward_pe=forward_pe, market_cap=market_cap, dividend_yield=dividend_yield,
                                  trailing_pe=trailing_pe)
                    stock.save()
