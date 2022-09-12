# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    PurchaseOrdersdf = spark.table(f"{DEFAULT_TARGET}.d_purchaseorders")
    PurchaseOrderLinesdf = spark.table(f"{DEFAULT_TARGET}.d_purchaseorderslines")
    Suppliers = spark.table(f"{DEFAULT_TARGET}.d_suppliers")
    
    # ------------- JOINS ------------------ #
    df = PurchaseOrdersdf.join(PurchaseOrderLinesdf, (PurchaseOrdersdf.PurchaseOrders_BK == PurchaseOrderLinesdf.PurchaseOrdersLines_BK), "inner")
    df = df.join(Suppliers, df.SupplierID == Suppliers.Suppliers_BK)
    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "PurchaseOrders_BK",
        "SupplierName",
        "PurchaseOrderLineID",
        "Description",
        "OrderedOuters",
        "ReceivedOuters",
        "ExpectedUnitPricePerOuter",
        "IsOrderLineFinalized"
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
