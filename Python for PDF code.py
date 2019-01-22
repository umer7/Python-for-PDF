
# coding: utf-8

# ## PyPDF2

# In[49]:


get_ipython().system('pip install PyPDF2')


# In[50]:


import PyPDF2 


# In[51]:


#!dir
pdfFileObj = open('sample.pdf', 'rb') 


# In[52]:


pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 


# In[53]:


print(pdfReader.numPages) 


# In[54]:


pageObj = pdfReader.getPage(1) 


# In[55]:


# creating a page object 
# extracting text from page 
print(pageObj.extractText())


# In[56]:


# of you want to store data into String
Pdf_String=pageObj.extractText()


# In[57]:


Pdf_String


# ## tabula
# ##### for Tabular Data

# In[58]:


get_ipython().system('pip install tabula-py')


# In[59]:


import tabula


# In[60]:


df = tabula.read_pdf("offense.pdf")


# In[62]:


df.head()


# #### for Mltiple Table

# In[63]:


df = tabula.read_pdf("data.pdf",multiple_tables=True)


# In[66]:


df


# ### For specific part 

# In[67]:


tabula.read_pdf("data.pdf", area=(126,149,212,462), pages=1)


# #### Json as Output Format

# In[70]:


tabula.read_pdf("data.pdf", output_format="json")


# ### Export into Excel or CSV

# In[71]:


tabula.convert_into("data.pdf", "data_excel.xlsx", output_format="xlsx")
# this will create data_excel.xlsx


# In[72]:


# for CSV export 
tabula.convert_into("data.pdf", "data_csv.csv", output_format="csv")
# this will create data_excel.csv

