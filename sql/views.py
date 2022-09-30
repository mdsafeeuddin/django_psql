from asyncio.log import logger
from django.http import HttpResponse
from django.db import connection
from django.template import loader
import logging

cursor = connection.cursor()
tables_list = ['departments', 'employees', 'regions']

def index(request):
  context = {
    'tables_list':tables_list
  }
  template = loader.get_template('sql/index.html')
  logging.warning("I'm in index")
  return HttpResponse(template.render(context, request))

def departments(request):
  cursor.execute('SELECT * FROM departments')
  dept_data = cursor.fetchall()
  context = {
    'tables_list':tables_list,
    'dept_data':dept_data
  }
  template = loader.get_template('sql/index.html')
  logging.warning("I'm in departments")
  return HttpResponse(template.render(context, request))

def employees(request):
  cursor.execute('SELECT * FROM employees')
  emp_data = cursor.fetchall()
  context = {
    'tables_list':tables_list,
    'emp_data':emp_data
  }
  template = loader.get_template('sql/index.html')
  return HttpResponse(template.render(context, request))

def regions(request):
  cursor.execute('SELECT * FROM regions')
  reg_data = cursor.fetchall()
  context = {
    'tables_list':tables_list,
    'reg_data':reg_data
  }
  template = loader.get_template('sql/index.html')
  return HttpResponse(template.render(context, request))


