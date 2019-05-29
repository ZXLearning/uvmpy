from uvm_void import uvm_void
from abc import ABCMeta,abstractmethod

class uvm_object(uvm_void):

	__metaclass__ = abc.ABCMeta
	m_inst_count = 0
	use_uvm_seeding = 1 
	
	def __init__(self, name):
		self.m_leaf_name = name
		self.__class__.m_inst_count += 1
		self.m_inst_id = self.__class__.m_inst_count
	@abstractmethod	
	def get_name(self):
		pass
	
	@abstractmethod	
	def set_name(name):
		pass
	
	@abstractmethod	
	def get_full_name(self):
		pass
	
	@abstractmethod	
	def get_inst_count(self):
		pass
	
	@abstractmethod	
	def get_inst_id(self):
		pass
	
	def reseed(self):
		pass
		
	@abstractmethod	
	def creat(self,name):
		pass
	
	def Print(self):
		pass
		
	def copy(self, rhs):
		pass
	
	@abstractmethod	
	def do_copy(self, rhs):
		pass
		
	def compare(self, rhs, comparer=None):
		pass
	
	@abstractmethod	
	def do_compare(self, rhs, comparer):
		pass		