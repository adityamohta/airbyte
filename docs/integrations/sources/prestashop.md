# PrestaShop

This page contains the setup guide and reference information for the PrestaShop source connector.

## Prerequisites

- Access Key
- Shop URL
- Start date

## Setup guide

### Step 1: Set up PrestaShop

1. By default, the webservice feature is disabled on PrestaShop and needs to be [switched on](https://devdocs.prestashop.com/1.7/webservice/tutorials/creating-access/#enable-the-webservice).
2. To get access to the PrestaShop API you need to create an access key, please follow the instructions in this [documentation](https://devdocs.prestashop-project.org/1.7/webservice/tutorials/creating-access/#create-an-access-key).

### Step 2: Set up the PrestaShop connector in Airbyte

**For Airbyte Cloud:**

1. [Log into your Airbyte Cloud](https://cloud.airbyte.com/workspaces) account.
2. In the left navigation bar, click **Sources**. In the top-right corner, click **+ new source**.
3. On the source setup page, select **PrestaShop** from the Source type dropdown and enter a name for this connector.
4. Enter the **Access Key** that you obtained.
5. Enter the **Shop URL** without trailing slash, for example, https://my.prestashop.com, only HTTPS urls are supported.
6. Enter **Start date** in YYYY-MM-DD format. The data added on and after this date will be replicated.

## Supported sync modes

The PrestaShop source connector supports the following [ sync modes](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):

- [Full Refresh - Overwrite](https://docs.airbyte.com/understanding-airbyte/connections/full-refresh-overwrite/)
- [Full Refresh - Append](https://docs.airbyte.com/understanding-airbyte/connections/full-refresh-append)
- [Incremental - Append](https://docs.airbyte.com/understanding-airbyte/connections/incremental-append)
- [Incremental - Append + Deduped](https://docs.airbyte.com/understanding-airbyte/connections/incremental-append-deduped)

## Supported Streams

This connector outputs the following full refresh streams:

- [Carriers](https://devdocs.prestashop.com/1.7/webservice/resources/carriers/)
- [Combinations](https://devdocs.prestashop.com/1.7/webservice/resources/combinations/)
- [Contacts](https://devdocs.prestashop.com/1.7/webservice/resources/contacts/)
- [Content Management System](https://devdocs.prestashop.com/1.7/webservice/resources/content_management_system/)
- [Countries](https://devdocs.prestashop.com/1.7/webservice/resources/countries/)
- [Currencies](https://devdocs.prestashop.com/1.7/webservice/resources/currencies/)
- [Deliveries](https://devdocs.prestashop.com/1.7/webservice/resources/deliveries/)
- [Employees](https://devdocs.prestashop.com/1.7/webservice/resources/employees/)
- [Guests](https://devdocs.prestashop.com/1.7/webservice/resources/guests/)
- [Image Types](https://devdocs.prestashop.com/1.7/webservice/resources/image_types/)
- [Languages](https://devdocs.prestashop.com/1.7/webservice/resources/languages/)
- [Order Details](https://devdocs.prestashop.com/1.7/webservice/resources/order_details/)
- [Order States](https://devdocs.prestashop.com/1.7/webservice/resources/order_states/)
- [Price Ranges](https://devdocs.prestashop.com/1.7/webservice/resources/price_ranges/)
- [Product Customization Fields](https://devdocs.prestashop.com/1.7/webservice/resources/product_customization_fields/)
- [Product Feature Values](https://devdocs.prestashop.com/1.7/webservice/resources/product_feature_values/)
- [Product Features](https://devdocs.prestashop.com/1.7/webservice/resources/product_features/)
- [Product Option Values](https://devdocs.prestashop.com/1.7/webservice/resources/product_option_values/)
- [Product Suppliers](https://devdocs.prestashop.com/1.7/webservice/resources/product_suppliers/)
- [ShopGroups](https://devdocs.prestashop.com/1.7/webservice/resources/shop_groups/)
- [ShopUrls](https://devdocs.prestashop.com/1.7/webservice/resources/shop_urls/)
- [Shops](https://devdocs.prestashop.com/1.7/webservice/resources/shops/)
- [Specific Price Rules](https://devdocs.prestashop.com/1.7/webservice/resources/specific_price_rules/)
- [Specific Prices](https://devdocs.prestashop.com/1.7/webservice/resources/specific_prices/)
- [States](https://devdocs.prestashop.com/1.7/webservice/resources/states/)
- [Stock Availables](https://devdocs.prestashop.com/1.7/webservice/resources/stock_availables/)
- [Tags](https://devdocs.prestashop.com/1.7/webservice/resources/tags/)
- [Tax Rules](https://devdocs.prestashop.com/1.7/webservice/resources/tax_rules/)
- [Taxes](https://devdocs.prestashop.com/1.7/webservice/resources/taxes/)
- [Translated Configurations](https://devdocs.prestashop.com/1.7/webservice/resources/translated_configurations/)
- [Weight Ranges](https://devdocs.prestashop.com/1.7/webservice/resources/weight_ranges/)
- [Zones](https://devdocs.prestashop.com/1.7/webservice/resources/zones/)

This connector outputs the following incremental streams:

- [Addresses](https://devdocs.prestashop.com/1.7/webservice/resources/addresses/)
- [Cart Rules](https://devdocs.prestashop.com/1.7/webservice/resources/cart_rules/)
- [Carts](https://devdocs.prestashop.com/1.7/webservice/resources/carts/)
- [Categories](https://devdocs.prestashop.com/1.7/webservice/resources/categories/)
- [Configurations](https://devdocs.prestashop.com/1.7/webservice/resources/configurations/)
- [Customer Messages](https://devdocs.prestashop.com/1.7/webservice/resources/customer_messages/)
- [Customer Threads](https://devdocs.prestashop.com/1.7/webservice/resources/customer_threads/)
- [Customers](https://devdocs.prestashop.com/1.7/webservice/resources/customers/)
- [Groups](https://devdocs.prestashop.com/1.7/webservice/resources/groups/)
- [Manufacturers](https://devdocs.prestashop.com/1.7/webservice/resources/manufacturers/)
- [Messages](https://devdocs.prestashop.com/1.7/webservice/resources/messages/)
- [Order Carriers](https://devdocs.prestashop.com/1.7/webservice/resources/order_carriers/)
- [Order Histories](https://devdocs.prestashop.com/1.7/webservice/resources/order_histories/)
- [Order Invoices](https://devdocs.prestashop.com/1.7/webservice/resources/order_invoices/)
- [Order Payments](https://devdocs.prestashop.com/1.7/webservice/resources/order_payments/)
- [Order Slip](https://devdocs.prestashop.com/1.7/webservice/resources/order_slip/)
- [Orders](https://devdocs.prestashop.com/1.7/webservice/resources/orders/)
- [Products](https://devdocs.prestashop.com/1.7/webservice/resources/products/)
- [Stock Movement Reasons](https://devdocs.prestashop.com/1.7/webservice/resources/stock_movement_reasons/)
- [Stock Movements](https://devdocs.prestashop.com/1.7/webservice/resources/stock_movements/)
- [Stores](https://devdocs.prestashop.com/1.7/webservice/resources/stores/)
- [Suppliers](https://devdocs.prestashop.com/1.7/webservice/resources/suppliers/)
- [Tax Rule Groups](https://devdocs.prestashop.com/1.7/webservice/resources/tax_rule_groups/)

If there are more endpoints you'd like Airbyte to support, please [create an issue.](https://github.com/airbytehq/airbyte/issues/new/choose)

## Changelog

<details>
  <summary>Expand to review</summary>

| Version | Date       | Pull Request                                              | Subject                                                                         |
| :------ | :--------- | :-------------------------------------------------------- | :------------------------------------------------------------------------------ |
| 1.2.6 | 2025-05-24 | [60072](https://github.com/airbytehq/airbyte/pull/60072) | Update dependencies |
| 1.2.5 | 2025-05-04 | [59516](https://github.com/airbytehq/airbyte/pull/59516) | Update dependencies |
| 1.2.4 | 2025-04-27 | [59044](https://github.com/airbytehq/airbyte/pull/59044) | Update dependencies |
| 1.2.3 | 2025-04-19 | [58487](https://github.com/airbytehq/airbyte/pull/58487) | Update dependencies |
| 1.2.2 | 2025-04-12 | [57916](https://github.com/airbytehq/airbyte/pull/57916) | Update dependencies |
| 1.2.1 | 2025-04-05 | [57334](https://github.com/airbytehq/airbyte/pull/57334) | Update dependencies |
| 1.2.0 | 2025-04-01 | [55739](https://github.com/airbytehq/airbyte/pull/55739) | Remove pendulum from dependency |
| 1.1.3 | 2025-03-29 | [56786](https://github.com/airbytehq/airbyte/pull/56786) | Update dependencies |
| 1.1.2 | 2025-03-22 | [56165](https://github.com/airbytehq/airbyte/pull/56165) | Update dependencies |
| 1.1.1 | 2025-03-08 | [43831](https://github.com/airbytehq/airbyte/pull/43831) | Update dependencies |
| 1.1.0 | 2025-03-03 | [47016](https://github.com/airbytehq/airbyte/pull/47016) | Migrate to manifest-only format |
| 1.0.4 | 2024-04-19 | [37233](https://github.com/airbytehq/airbyte/pull/37233) | Updating to 0.80.0 CDK |
| 1.0.3 | 2024-04-18 | [37233](https://github.com/airbytehq/airbyte/pull/37233) | Manage dependencies with Poetry. |
| 1.0.2 | 2024-04-15 | [37233](https://github.com/airbytehq/airbyte/pull/37233) | Base image migration: remove Dockerfile and use the python-connector-base image |
| 1.0.1 | 2024-04-12 | [37233](https://github.com/airbytehq/airbyte/pull/37233) | schema descriptions |
| 1.0.0 | 2023-06-26 | [27716](https://github.com/airbytehq/airbyte/pull/27716) | update schema; remove empty datetime fields |
| 0.3.1 | 2023-02-13 | [22905](https://github.com/airbytehq/airbyte/pull/22905) | Specified date formatting in specification |
| 0.3.0   | 2022-11-08 | [#18927](https://github.com/airbytehq/airbyte/pull/18927) | Migrate connector from Alpha (Python) to Beta (YAML)                            |
| 0.2.0   | 2022-10-31 | [#18599](https://github.com/airbytehq/airbyte/pull/18599) | Only https scheme is allowed                                                    |
| 0.1.0   | 2021-07-02 | [#4465](https://github.com/airbytehq/airbyte/pull/4465)   | Initial implementation                                                          |

</details>
