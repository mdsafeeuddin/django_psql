from django.http import HttpResponse
from django.db import connection
from django.template import loader
import logging
import pandas as pd
from .models import Section

cursor = connection.cursor()
tables_list = ['departments', 'employees', 'regions']
sections_topics = Section.objects.all().values()

def index(request):
  cursor.execute('select section_title, topic, topics.id, sections.created as section_created, topics.created as topic_created\
                 from topics\
                 right outer join sections on sections.id = topics.section_id\
                 order by section_created asc')
  section_topics = cursor.fetchall()
  sectops_df = pd.DataFrame(section_topics, columns=['section_title', 'topic', 'duration', 'section_created', 'topic_created'])
  sectops_data = sectops_df.groupby('section_title')['topic'].apply(list).to_dict()
  
  cursor.execute('select section_title from sections order by created asc')
  sections = cursor.fetchall()
  ordered_sections = [''.join(k) for k in sections]

  reordered_sectops = {k: sectops_data[k] for k in ordered_sections}
  print(reordered_sectops)
  context = {
    'tables_list':tables_list,
    'sections_list': sections_topics,
    'sectops':reordered_sectops
  }
  template = loader.get_template('sql/index.html')
  return HttpResponse(template.render(context, request))

def departments(request):
  cursor.execute('SELECT * FROM departments')
  dept_data = cursor.fetchall()
  dept_df = pd.DataFrame(dept_data, columns=['department', 'division'])
  dept_df = dept_df.style.set_table_styles([dict(selector='th', props=[('border', '1px black solid !important '),('text-align', 'center')])])
  dept_df.set_properties(**{'text-align': 'center', 'border':'1px black solid !important'}).hide_index()
  context = {
    'tables_list':tables_list,
    'sections_list': sections_topics,
    'dept_data':dept_df.to_html()
  }
  template = loader.get_template('sql/index.html')
  logging.warning("I'm in departments")
  return HttpResponse(template.render(context, request))

def employees(request):
  cursor.execute('SELECT * FROM employees')
  emp_data = cursor.fetchall()
  emp_df = pd.DataFrame(emp_data, columns=['employee_id', 'first_name', 'last_name', 'email', 'hire_date', 'department', 'gender', 'salary', 'region'] )
  emp_df = emp_df.style.set_table_styles([dict(selector='th', props=[('border', '1px black solid !important'), ('text-align', 'center')])])
  emp_df.set_properties(**{'text-align': 'center', 'border':'1px black solid !important'}).hide_index()
  context = {
    'tables_list':tables_list,
    'sections_list': sections_topics,
    'emp_data':emp_df.to_html()
  }
  template = loader.get_template('sql/index.html')
  return HttpResponse(template.render(context, request))

def regions(request):
  cursor.execute('SELECT * FROM regions')
  reg_data = cursor.fetchall()
  reg_df = pd.DataFrame(reg_data, columns=['region_id', 'region', 'country'])
  reg_df = reg_df.style.set_table_styles([dict(selector='th', props=[('border', '1px black solid !important'), ('text-align', 'center')])])
  reg_df.set_properties(**{'text-align': 'center', 'border':'1px black solid !important'}).hide_index()
  context = {
    'tables_list':tables_list,
    'sections_list': sections_topics,
    'reg_data':reg_df.to_html()
  }
  template = loader.get_template('sql/index.html')
  return HttpResponse(template.render(context, request))


