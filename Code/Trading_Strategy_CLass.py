
class Trading_Strategy():

	def __init__(self, data, 
					   main, 
					   upper_band, 
					   lower_band):
		'''Trading Strategy based on bands 
		'''
		self.data =data 
		self.main = main	
		self.upper_band = upper_band, 
		self.lower_band = lower_band

		self.setting()
		self.apply_entry_position()

	def setting(self):
		self.data['SIGNAL'] = 0 
		self.data['POSITION'] = 0 	

	def long(self):
		long_position = ((self.data[self.main].shift(1) < self.data[self.lower_band]) 
                            & (self.data[self.main] > self.data[self.lower_band]))
		self.data.loc[long_entry_condition, 'SIGNAL'] = 1

	def short():
		short_position = ((self.data[self.main].shift(1) > self.data[self.upper_band])
                            & (self.data[self.main] < self.data[self.main]))

		self.data.loc[short_position, 'SIGNAL'] = - 1
