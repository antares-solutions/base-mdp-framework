# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"trusted.sales_orders")
    # ------------- JOINS ------------------ #

    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "OrderID SalesOrders_BK",
        "CustomerID",
        "SalespersonPersonID",
        "PickedByPersonID",
        "ContactPersonID",
        "BackorderOrderID",
        "OrderDate",
        "ExpectedDeliveryDate",
        "CustomerPurchaseOrderNumber",
        "IsUndersupplyBackordered",
        "Comments",
        "DeliveryInstructions",
        "InternalComments",
        "PickingCompletedWhen",
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
