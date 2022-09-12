# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"trusted.sales_invoices")
    # ------------- JOINS ------------------ #

    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "InvoiceID SalesInvoices_BK",
        "CustomerID",
        "BillToCustomerID",
        "OrderID",
        "DeliveryMethodID",
        "ContactPersonID",
        "AccountsPersonID",
        "SalespersonPersonID",
        "PackedByPersonID",
        "InvoiceDate",
        "CustomerPurchaseOrderNumber",
        "IsCreditNote",
        "CreditNoteReason",
        "Comments",
        "DeliveryInstructions",
        "InternalComments",
        "TotalDryItems",
        "TotalChillerItems",
        "DeliveryRun",
        "RunPosition",
        "ReturnedDeliveryData",
        "ConfirmedDeliveryTime",
        "ConfirmedReceivedBy",
        "LastEditedBy",
        "LastEditedWhen"
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

# COMMAND ----------


