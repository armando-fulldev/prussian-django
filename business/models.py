from django.db import models

class Business_Basic_Info(models.Model):
    #org_entity_id = ...
    website = models.CharField(max_length=30)
    number_of_employees = models.IntegerField()
    description_of_business = models.CharField(max_length=50)

    ### foreign key area.
    pass
class Business_Condition(models.Model):
    ### own variables area.
    company_formation = models.CharField(max_length=50)
    business_model = models.CharField(max_length=50)
    leverage_on_tech = models.CharField(max_length=50)
    competitiveness_1 = models.CharField(max_length=50)
    competitiveness_2 = models.CharField(max_length=50)
    competitiveness_3 = models.CharField(max_length=50)
    growth_1 = models.CharField(max_length=50)
    growth_2 = models.CharField(max_length=50)
    growth_3 = models.CharField(max_length=50)
    top_risk_1 = models.CharField(max_length=50)
    top_risk_2 = models.CharField(max_length=50)
    top_risk_3 = models.CharField(max_length=50)
    rival_sector = models.CharField(max_length=50)
    competitor_1 = models.CharField(max_length=50)
    competitor_2 = models.CharField(max_length=50)
    competitor_3 = models.CharField(max_length=50)
    supplychain_risk = models.CharField(max_length=50)

    ### foreign key area.
    business_basic_info_id = models.OneToOneField(Business_Basic_Info, on_delete=models.CASCADE)
class Cashflow(models.Model):
    ### own variable area.
    operating_cash_flow = models.IntegerField()
    cash_flow_from_continuing_operating_activities = models.IntegerField()
    net_income_from_continuing_operations = models.IntegerField()
    operating_gains_losses = models.IntegerField()
    depreciation_amortization_depletion = models.IntegerField()
    depreciation_and_amortization = models.IntegerField()
    deferred_tax = models.IntegerField()
    deferred_income_tax = models.IntegerField()
    provision_and_write_off_of_assets = models.IntegerField()
    stock_based_compensation = models.IntegerField()
    excess_tax_benefit_from_stock_based_compensation = models.IntegerField()
    other_non_cash_items = models.IntegerField()
    change_in_working_capital = models.IntegerField()
    change_in_receivables = models.IntegerField()
    change_in_account_receivables = models.IntegerField()
    change_in_inventory = models.IntegerField()
    change_in_payables_and_accrued_expense = models.IntegerField()
    change_in_other_current_liabilities = models.IntegerField()
    change_in_other_working_capital = models.IntegerField()
    investing_cash_flow = models.IntegerField()
    cash_flow_from_continuing_investing_activities = models.IntegerField()
    capital_expenditure_reported = models.IntegerField()
    net_business_purchase_and_sale = models.IntegerField()
    purchase_of_business = models.IntegerField()
    net_investment_purchase_and_sale = models.IntegerField()
    purchase_of_investment = models.IntegerField()
    sale_of_investment = models.IntegerField()
    net_other_investing_changes = models.IntegerField()
    financing_cash_flow = models.IntegerField()
    cash_flow_from_continuing_financing_activities = models.IntegerField()
    net_issuance_payments_of_debt = models.IntegerField()
    net_long_term_debt_issuance = models.IntegerField()
    long_term_debt_issuance = models.IntegerField()
    long_term_debt_payments = models.IntegerField()
    net_common_stock_issuance = models.IntegerField()
    common_stock_payments = models.IntegerField()
    cash_dividends_paid = models.IntegerField()
    common_stock_dividened_paid = models.IntegerField()
    proceeds_from_stock_option_exercised = models.IntegerField()
    net_other_financing_charges = models.IntegerField()
    end_cash_position = models.IntegerField()
    changes_in_cash = models.IntegerField()
    effect_of_exchange_rate_changes = models.IntegerField()
    beginning_cash_position = models.IntegerField()
    other_cash_adjustment_outside_change_in_cash = models.IntegerField()
    capital_expenditure = models.IntegerField()
    issuance_of_debt = models.IntegerField()
    repayment_of_debt = models.IntegerField()
    repurchase_of_capital_Stock = models.IntegerField()
    free_cash_flow = models.IntegerField()

    ### foreign key area.
    pass

class Balance_sheet(models.Model):
    ### own variable area.
    total_assets = models.IntegerField()
    current_assets = models.IntegerField()
    cash_equivalents_and_short_term_investments = models.IntegerField()
    cash_and_cash_equivalents = models.IntegerField()
    receivables = models.IntegerField()
    accounts_receivable = models.IntegerField()
    gross_accounts_receivable = models.IntegerField()
    allowance_for_doubtful_accounts_receivable = models.IntegerField()
    inventory = models.IntegerField()
    raw_materials = models.IntegerField()
    finished_goods = models.IntegerField()
    other_inventories = models.IntegerField()
    prepaid_assets = models.IntegerField()
    restricted_cash = models.IntegerField()
    other_current_assets = models.IntegerField()
    total_non_current_assets = models.IntegerField()
    net_ppe = models.IntegerField()
    gross_ppe = models.IntegerField()
    properties = models.IntegerField()
    land_and_improvements = models.IntegerField()
    machinery_furniture_equipment = models.IntegerField()
    other_properties = models.IntegerField()
    construction_in_progress = models.IntegerField()
    leases = models.IntegerField()
    accumulated_depreciation = models.IntegerField()
    goodwill_and_other_intangible_assets = models.IntegerField()
    goodwill = models.IntegerField()
    other_intangible_assets = models.IntegerField()
    investments_and_advances = models.IntegerField()
    investment_in_financial_assets = models.IntegerField()
    trading_securities = models.IntegerField()
    non_current_deferred_assets = models.IntegerField()
    non_current_deffered_taxes_assets = models.IntegerField()
    other_non_current_assets = models.IntegerField()
    total_liabilities_net_minority_interest = models.IntegerField()
    current_liabilities = models.IntegerField()
    payables_and_accrued_expenses = models.IntegerField()
    payables = models.IntegerField()
    accounts_payable = models.IntegerField()
    current_accured_expenses = models.IntegerField()
    interest_payable = models.IntegerField()
    current_provisions = models.IntegerField()
    pesion_and_other_post_retirement_benefit_plans_current = models.IntegerField()
    current_debt_and_capital_lease_obligation = models.IntegerField()
    current_debt = models.IntegerField()
    other_current_borrowings = models.IntegerField()
    current_capital_lease_obligation = models.IntegerField()
    other_current_liabilities = models.IntegerField()
    total_non_current_liabilities_net_minority_interest = models.IntegerField()
    long_term_provisions = models.IntegerField()
    long_term_debt_and_capital_lease_obligation = models.IntegerField()
    long_term_debt = models.IntegerField()
    long_term_capital_lease_obligation = models.IntegerField()
    non_current_deferred_liabilities = models.IntegerField()
    non_current_deferred_taxes_liabilities = models.IntegerField()
    non_current_accrued_expenses = models.IntegerField()
    total_equity_gross_minority_interest = models.IntegerField()
    stockholders_equity = models.IntegerField()
    capital_stock = models.IntegerField()
    preferred_stock = models.IntegerField()
    common_stock = models.IntegerField()
    additional_paid_in_capital = models.IntegerField()
    retained_earnings = models.IntegerField()
    gains_losses_not_affecting_retained_earnings = models.IntegerField()
    total_capitalization = models.IntegerField()
    common_stock_equity = models.IntegerField()
    capital_lease_obligations = models.IntegerField()
    net_tangible_assets = models.IntegerField()
    working_capital = models.IntegerField()
    invested_capital = models.IntegerField()
    tangible_book_value = models.IntegerField()
    total_debt = models.IntegerField()
    net_debt = models.IntegerField()
    share_issued = models.IntegerField()
    ordinary_shares_number = models.IntegerField()

    ### foreign key area.
    pass

class Income_Statement(models.Model):
    ### own variable area.
    total_revenue = models.IntegerField()
    operating_revenue = models.IntegerField()
    cost_of_revenue = models.IntegerField()
    gross_profit = models.IntegerField()
    operating_expense = models.IntegerField()
    selling_general_and_administrative = models.IntegerField()
    general_and_administrative_expense = models.IntegerField()
    other_g_and_a = models.IntegerField()
    selling_and_marketing_expense = models.IntegerField()
    operating_income = models.IntegerField()
    net_non_operating_interest_income_expense = models.IntegerField()
    interest_income_non_operating = models.IntegerField()
    interest_expense_non_operating = models.IntegerField()
    pretax_income = models.IntegerField()
    net_income_common_stockholders = models.IntegerField()
    net_income = models.IntegerField()
    net_income_including_non_controlling_interests = models.IntegerField()
    net_income_continuous_operations = models.IntegerField()
    diluted_ni_available_to_com_stockholders = models.IntegerField()
    basic_eps = models.IntegerField()
    diluted_eps = models.IntegerField()
    basic_average_shares = models.IntegerField()
    diluted_average_shares = models.IntegerField()
    total_operating_income_as_reported = models.IntegerField()
    total_expenses = models.IntegerField()
    net_income_from_continuing_and_discontinued_opertaions = models.IntegerField()
    normalized_income = models.IntegerField()
    interest_income = models.IntegerField()
    interest_expense = models.IntegerField()
    net_interest_income = models.IntegerField()
    ebit = models.IntegerField()
    ebitda = models.IntegerField()
    reconciled_cost_of_revenue = models.IntegerField()
    reconciled_depreciation = models.IntegerField()
    net_income_from_continuing_operation_net_minority_interest = models.IntegerField()
    normalized_ebitda = models.IntegerField()
    tax_rate_for_calcs = models.IntegerField()
    tax_effect_of_unusual_items = models.IntegerField()

    ### foreign key area.
    pass
class Business_Finance(models.Model):
    ### own variable area.
    annual_gross_revenue = models.CharField(max_length=50)
    annual_gross_profit = models.CharField(max_length=50)
    cash_ratio = models.CharField(max_length=50)
    quick_ratio = models.CharField(max_length=50)
    cash_position = models.CharField(max_length=50)
    annual_free_cashflow = models.CharField(max_length=50)
    total_debt = models.CharField(max_length=50)
    month_of_fiscal_year_end = models.CharField(max_length=50)
    total_business_worth = models.CharField(max_length=50)

    ### foreign key area.
    business_basic_info_id = models.ForeignKey(Business_Basic_Info, on_delete=models.CASCADE)
    cashflow_id = models.OneToOneField(Cashflow, on_delete=models.CASCADE)
    balance_sheet_id = models.OneToOneField(Balance_sheet, on_delete=models.CASCADE)
    income_statement_id = models.OneToOneField(Income_Statement, on_delete=models.CASCADE)

class Business_Preference(models.Model):
    ### own variable area.
    risk_tolerance = models.CharField(max_length=50)
    expected_duration = models.CharField(max_length=50)
    investor_type = models.CharField(max_length=50)
    preferred_sector_1 = models.CharField(max_length=50)
    preferred_sector_2 = models.CharField(max_length=50)
    preferred_sector_3 = models.CharField(max_length=50)
    target_cash_balance = models.CharField(max_length=50)
    disliked_asset_class_1 = models.CharField(max_length=50)
    disliked_asset_class_2 = models.CharField(max_length=50)
    disliked_asset_class_3 = models.CharField(max_length=50)
    interested_asset_class_1 = models.CharField(max_length=50)
    interested_asset_class_2 = models.CharField(max_length=50)
    interested_asset_class_3 = models.CharField(max_length=50)
    country_refused_1 = models.CharField(max_length=50)
    country_refused_2 = models.CharField(max_length=50)
    country_refused_3 = models.CharField(max_length=50)
    country_interested_1 = models.CharField(max_length=50)
    country_interested_2 = models.CharField(max_length=50)
    country_interested_3 = models.CharField(max_length=50)
    projected_major_spending = models.CharField(max_length=50)
    projected_spending_amt = models.CharField(max_length=50)
    cash_set_aside = models.CharField(max_length=50)
    _100k_1m_50percent = models.CharField(max_length=50)
    _100k_500k_50percen = models.CharField(max_length=50)
    how_often_availability = models.CharField(max_length=50)

    ### foreign key area.
    business_basic_info_id = models.OneToOneField(Business_Basic_Info, on_delete=models.CASCADE)


#### Financial risk analysis ####

class Risk_Weight(models.Model):
    ### own variable area.
    risk_weight_coefficient = models.CharField(max_length=50)

    ### foreign key area.
    pass

class Business_Systemic_Risk(models.Model):
    ### own variable area.
    broader_index_risk_level = models.CharField(max_length=50)
    sector_index_risk_level = models.CharField(max_length=50)
    broader_index_correlation_level = models.CharField(max_length=50)
    sector_index_correlation_level = models.CharField(max_length=50)
    contrarian_level = models.CharField(max_length=50)
    macro_risk_level = models.CharField(max_length=50)
    sector_rotation_risk_level = models.CharField(max_length=50)
    last_updated = models.CharField(max_length=50)

    ### foreign key area.
    risk_weight_id = models.ForeignKey(Risk_Weight, on_delete=models.CASCADE)
    business_basic_info_id = models.OneToOneField(Business_Basic_Info, on_delete=models.CASCADE)

class Business_Structural_Risk(models.Model):
    ### own variable area.
    tech_transformation_risk_level = models.CharField(max_length=50)
    seasonality_risk_level = models.CharField(max_length=50)
    new_vs_old_economy = models.CharField(max_length=50)
    geopolitical_risk_level = models.CharField(max_length=50)
    policy_risk_level = models.CharField(max_length=50)
    product_competitiveness_risk_level = models.CharField(max_length=50)
    business_DNA_risk_level = models.CharField(max_length=50)
    contrarian_level = models.CharField(max_length=50)
    overproduction_risk_level = models.CharField(max_length=50)
    last_updated = models.CharField(max_length=50)

    ### foreign key area.
    risk_weight_id = models.ForeignKey(Risk_Weight, on_delete=models.CASCADE)
    business_basic_info_id = models.OneToOneField(Business_Basic_Info, on_delete=models.CASCADE)

class Business_Conditional_Risk(models.Model):
    ### own variable area.
    total_conditional_event_risk_level = models.CharField(max_length=50)
    total_event_correlation_risk_level = models.CharField(max_length=50)
    total_new_competition_risk_level = models.CharField(max_length=50)
    total_new_opportunity_risk_level = models.CharField(max_length=50)
    last_updated = models.CharField(max_length=50)

    ### foreign key area.
    risk_weight_id = models.ForeignKey(Risk_Weight, on_delete=models.CASCADE)
    business_basic_info_id = models.OneToOneField(Business_Basic_Info, on_delete=models.CASCADE)

class Hedgeability(models.Model):
    ### own variable area.
    risk_clarity_level = models.CharField(max_length=50)
    risk_quantifiability_level = models.CharField(max_length=50)
    free_cash_liquidity = models.CharField(max_length=50)
    risk_hedge_correlation_clarity_level = models.CharField(max_length=50)
    risk_hedge_correlation_quantifiability_level = models.CharField(max_length=50)
    overall_hedgeability_level = models.CharField(max_length=50)

    ### foreign key area.
    business_systemic_risk_id = models.ManyToManyField(Business_Systemic_Risk)
    business_structural_risk_id = models.ManyToManyField(Business_Structural_Risk)
    business_conditional_risk_id = models.ManyToManyField(Business_Conditional_Risk)
    business_condition_id = models.ManyToManyField(Business_Condition)
    business_preference_id = models.ManyToManyField(Business_Preference)
    business_finance_id = models.ManyToManyField(Business_Finance)