# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"trusted.sales_customers")
    # ------------- JOINS ------------------ #

    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "CustomerID SalesCustomers_BK",
        "CustomerName",
        "BillToCustomerID",
        "CustomerCategoryID",
        "BuyingGroupID",
        "PrimaryContactPersonID",
        "AlternateContactPersonID",
        "DeliveryMethodID",
        "DeliveryCityID",
        "PostalCityID",
        "CreditLimit",
        "AccountOpenedDate",
        "StandardDiscountPercentage",
        "IsStatementSent",
        "IsOnCreditHold",
        "PaymentDays",
        "PhoneNumber",
        "FaxNumber",
        "DeliveryRun",
        "RunPosition",
        "WebsiteURL",
        "DeliveryAddressLine1",
        "DeliveryAddressLine2",
        "DeliveryPostalCode",
        "PostalAddressLine1",
        "PostalAddressLine2",
        "PostalPostalCode",
        "LastEditedBy"
    ]
    
    df = df.selectExpr(
        _.Transforms
    )

    # ------------- CLAUSES ---------------- #

    # ------------- SAVE ------------------- #
    #display(df)
    Save(df)

pass

Transform()    
