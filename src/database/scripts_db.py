INSERT_TABLE_LEADS = '''
      INSERT INTO public.projeto_kurier_leads(
          lead_id
        , created_at
        , status
        , contact_name
        , contact_email
        , contact_phone
        , marketing_channel
        , marketing_utm
        , metadata_score
        , metadata_duplicate
        , metadata_test
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

INSERT_TABLE_CLIENTES = '''
    INSERT INTO projeto_kurier_clientes (
    client_id
  , email       
  , name_lead     
  , converted_at  
  , status        
  , segment       
  , internal_notes
  , origin_lead_id
  , origin_channel
  , owner_name    
  , owner_team) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

INSERT_TABLE_VENDAS = """
    INSERT INTO projeto_kurier_vendas(
      sale_id            
    , client_id	         
    , sale_date          
    , amount             
    , status	         
    , product            
    , payment_method     
    , payment_installment
    , extra_discount     
    , extra_notes        
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
"""

CREATE_TABLE_LEADS = '''
CREATE TABLE public.projeto_kurier_leads (
    lead_id TEXT,
    created_at DATE,
    status TEXT,
    contact_name TEXT,
    contact_email TEXT,
    contact_phone TEXT,
    marketing_channel TEXT,
    marketing_utm TEXT,
    metadata_score INT,
    metadata_duplicate BOOLEAN,
    metadata_test BOOLEAN
);
'''

CREATE_TABLE_CLIENTES = '''
CREATE TABLE projeto_kurier_clientes(
	client_id      text NOT NULL PRIMARY KEY
  , email          text
  , name_lead      text
  , converted_at   date
  , status         text
  , segment        text
  , internal_notes text
  , origin_lead_id text
  , origin_channel text
  , owner_name     text
  , owner_team     text
  );
'''

CREATE_TABLE_VENDAS = '''
    CREATE TABLE projeto_kurier_vendas(
      sale_id             text NOT NULL PRIMARY KEY
    , client_id	          text
    , sale_date           date
    , amount              bigint
    , status	          text
    , product             text
    , payment_method      text
    , payment_installment int
    , extra_discount      int
    , extra_notes         text
    );
'''