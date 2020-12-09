from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from boards.models import boards

class BoardsSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return boards.objects.filter(valid=True)

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['home', 'boards', 'colleges','register']

    def location(self, item):
        return reverse(item)

class CollegesSitemap(Sitemap):
    changefreq = "weekly"

    def iyems(self):
        return colleges.objects.filter(valid=True)