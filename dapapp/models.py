from django.db import models
from django.contrib.auth.models import User


class County(models.Model):
	countyname = models.CharField(max_length=100)
	code = models.IntegerField()
	def __str__(self):
		return self.countyname
	class Meta:
		verbose_name = 'County'
		verbose_name_plural = 'Counties'

	@property
	def subcountydata(self):
		data = self.subcounty_set.all()

		return data
	

class Subcounty(models.Model):
	county = models.ForeignKey(County, on_delete=models.CASCADE)
	subcountyname = models.CharField(max_length=100)

	def __str__(self):
		return self.subcountyname


	class Meta:
		verbose_name = 'Subcounty'
		verbose_name_plural = 'Subcounties'

	@property
	def subcountydeliveries(self):
		total = self.deliveries_set.all()
		return total
	



class DeliveriesInfo(models.Model):
	subcountyname = models.ForeignKey(Subcounty, on_delete=models.CASCADE)
	facilityname = models.ForeignKey(User, on_delete=models.CASCADE)
	noofsuccessfulbirths = models.IntegerField()
	nooflivebirths =models.IntegerField()
	noofstillbirths = models.IntegerField()
	dateentered = models.DateField(auto_now_add = True)
	def __str__(self):
		return '%s, %s'%(self.facilityname, self.dateentered)

	class Meta:
		verbose_name = 'DeliveriesInfo Table'
		verbose_name_plural = 'DeliveriesInfo Table'

	@property
	def mortality_rate(self):
		rates = self.maternaldeaths.x_sum / self.nooflivebirths
		rate = rate * rates
		return rate
	

class MaternalDeathsInfo(models.Model):
	deliveries = models.ForeignKey(DeliveriesInfo, on_delete=models.CASCADE)
	hemorrhage = models.IntegerField(default=0)
	infections = models.IntegerField(default=0)
	hypertension = models.IntegerField(default=0)
	delivery_complication = models.IntegerField(default=0)
	unsafe_abortions = models.IntegerField(default=0)

	def __str__(self):
		return str(self.deliveries.facilityname)

	@property
	def x_sum(self):
		total = self.hemorrhage + self.infections + self.hypertension + self.delivery_complication + self.unsafe_abortions

		return total
	



