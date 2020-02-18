#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
"""
Instead of using the normal statements to access attributes, 
you can use the following functions
    - The getattr(obj, name[, default]) − to access the attribute of object.
    - The hasattr(obj,name) − to check if an attribute exists or not.
    - The setattr(obj,name,value) − to set an attribute. If attribute does not exist, 
      then it would be created.
    - The delattr(obj, name) − to delete an attribute.
    
Built-In Class Attributes
  - Every Python class keeps following built-in attributes and they can be accessed
      using dot operator like any other attribute −

    * __dict__ − Dictionary containing the class's namespace.
    * __doc__ − Class documentation string or none, if undefined.
    * __name__ − Class name.
    * __module__ − Module name in which the class is defined. 
      This attribute is "__main__" in interactive mode.
    * __bases__ − A possibly empty tuple containing the base classes, 
      in the order of their occurrence in the base class list.
    
"""
