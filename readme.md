# recommendation api
## content.
*  How to run app
*  Api Documentaion

Code Structure
=====================================
1. Clone git repo https://github.com/sfwat/recommendation_api.git
2. Make sure you are on master branch **$git checkout master**
3. Create and activate Virual enviroment **$virtualenv venv**    **source/venv/bin/activate**
4. Move to recommendation api dir and install packages from requirments file $ pip install -r requirments.txt
5. Run the run.py file

Api Documentaion
=====================================
## product recommendation [/product_reco] 


### product recommendation [POST]

+ Request

    + Schema  
            
             {
            "title": "User",
            "type": "object",
            "maxProperties": 8,
            "additionalProperties": False,
            "properties": {
                    "gender": {
                        "type": "string",
                        "enum": ["H", "V"]
                        },
                    "age": {
                        "type": "number"
                    },
                    "annual_income": {
                        "type": "number"
                    },
                    "region": {
                        "type": "string"
                    },
                    "activity_level": {
                        "type": "string",
                        "enum": ["1", "0"]
                    },
                    "segment": {
                        "type": "string",
                        "enum": ["01 - TOP", "02 - PARTICULARES", "03 - UNIVERISTARIO"]
                    },
                    "seniority": {
                        "type": "number"
                    },
                    "relationship_type": {
                        "type":"string",
                        "enum": ["A", "I"]
                    }
                }
            }
+ First Body
    
           {
               "age": 30,
               "gender": "H",
               "region": "MADRID",
               "seniority": 256,
               "relationship_type": "A",
               "activity_level": "1",
               "annual_income": 95265,
               "segment": "02 - PARTICULARES"
           }

+ First Response 200 (application/json)

    + Body
    
            {
                "recommendations": {
                    "product1": "Current Accounts",
                    "product2": "Payroll",
                    "product3": "Direct Debit",
                    "product4": "Credit Card",
                    "product5": "Pensions",
                    "product6": "Payroll Account",
                    "product7": "e-account"
                    }
            }

+  Second Body
    
            {
                "age": 22,
                "gender": "V",
                "region": "BARCELONA",
                "seniority": 240,
                "relationship_type": "I",
                "activity_level": "1",
                "annual_income": 88000,
                "segment": "01 - TOP"
            }


+ Second Response 200 (application/json)

    + Body
    
            {
                "recommendations": {
                    "product1": "Current Accounts",
                    "product2": "Payroll",
                    "product3": "Pensions",
                    "product4": "Direct Debit",
                    "product5": "Payroll Account",
                    "product6": "e-account",
                    "product7": "Credit Card"
                }
            }

 +  Third Body
    
            {
                "age": 40,
                "gender": "H",
                "region": "ZARAGOZA",
                "seniority": 500,
                "relationship_type": "I",
                "activity_level": "0",
                "annual_income": 1200000,
                "segment": "01 - TOP"
            }


+ Third Response 200 (application/json)

    + Body
    
            {
                "recommendations": {
                "product1": "Current Accounts",
                "product2": "Credit Card",
                "product3": "Direct Debit",
                "product4": "e-account",
                "product5": "Taxes",
                "product6": "Pensions",
                "product7": "Payroll"
                }
            }