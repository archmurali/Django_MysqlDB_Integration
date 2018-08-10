# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class OcAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    company = models.CharField(max_length=40)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_address'


class OcAffiliate(models.Model):
    affiliate_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    company = models.CharField(max_length=40)
    website = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    code = models.CharField(max_length=64)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.CharField(max_length=64)
    payment = models.CharField(max_length=6)
    cheque = models.CharField(max_length=100)
    paypal = models.CharField(max_length=64)
    bank_name = models.CharField(max_length=64)
    bank_branch_number = models.CharField(max_length=64)
    bank_swift_code = models.CharField(max_length=64)
    bank_account_name = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate'


class OcAffiliateActivity(models.Model):
    affiliate_activity_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_activity'


class OcAffiliateLogin(models.Model):
    affiliate_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_login'


class OcAffiliateTransaction(models.Model):
    affiliate_transaction_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_transaction'


class OcAgentCommission(models.Model):
    agent_id = models.IntegerField(blank=True, null=True)
    customer_course_id = models.IntegerField(blank=True, null=True)
    commission_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_agent_commission'


class OcAgentDefaultCommission(models.Model):
    agent_id = models.IntegerField(blank=True, null=True)
    commission_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_agent_default_commission'


class OcAmazonLoginPayOrder(models.Model):
    amazon_login_pay_order_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    amazon_order_reference_id = models.CharField(max_length=255)
    amazon_authorization_id = models.CharField(max_length=255)
    free_shipping = models.IntegerField()
    date_added = models.DateTimeField()
    modified = models.DateTimeField()
    capture_status = models.IntegerField(blank=True, null=True)
    cancel_status = models.IntegerField(blank=True, null=True)
    refund_status = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_amazon_login_pay_order'


class OcAmazonLoginPayOrderTotalTax(models.Model):
    order_total_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_amazon_login_pay_order_total_tax'


class OcAmazonLoginPayOrderTransaction(models.Model):
    amazon_login_pay_order_transaction_id = models.AutoField(primary_key=True)
    amazon_login_pay_order_id = models.IntegerField()
    amazon_authorization_id = models.CharField(max_length=255, blank=True, null=True)
    amazon_capture_id = models.CharField(max_length=255, blank=True, null=True)
    amazon_refund_id = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField()
    type = models.CharField(max_length=13, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_amazon_login_pay_order_transaction'


class OcApi(models.Model):
    api_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    key = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api'


class OcApiIp(models.Model):
    api_ip_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'oc_api_ip'


class OcApiSession(models.Model):
    api_session_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    token = models.CharField(max_length=32)
    session_id = models.CharField(max_length=32)
    session_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api_session'


class OcAttribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute'


class OcAttributeDescription(models.Model):
    attribute_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_description'
        unique_together = (('attribute_id', 'language_id'),)


class OcAttributeGroup(models.Model):
    attribute_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute_group'


class OcAttributeGroupDescription(models.Model):
    attribute_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_group_description'
        unique_together = (('attribute_group_id', 'language_id'),)


class OcBanner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner'


class OcBannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    banner_id = models.IntegerField()
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner_image'


class OcBannerImageDescription(models.Model):
    banner_image_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    banner_id = models.IntegerField()
    title = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_banner_image_description'
        unique_together = (('banner_image_id', 'language_id'),)


class OcCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    product_id = models.IntegerField()
    recurring_id = models.IntegerField()
    option = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_cart'


class OcCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_category'


class OcCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_category_description'
        unique_together = (('category_id', 'language_id'),)


class OcCategoryFilter(models.Model):
    category_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_filter'
        unique_together = (('category_id', 'filter_id'),)


class OcCategoryPath(models.Model):
    category_id = models.IntegerField(primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_path'
        unique_together = (('category_id', 'path_id'),)


class OcCategoryToLayout(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_layout'
        unique_together = (('category_id', 'store_id'),)


class OcCategoryToStore(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_store'
        unique_together = (('category_id', 'store_id'),)


class OcCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)
    address_format = models.TextField()
    postcode_required = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_country'


class OcCountryButtons(models.Model):
    information_id = models.IntegerField(blank=True, null=True)
    button_number = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_country_buttons'


class OcCoupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=1)
    discount = models.DecimalField(max_digits=15, decimal_places=4)
    logged = models.IntegerField()
    shipping = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()
    uses_total = models.IntegerField()
    uses_customer = models.CharField(max_length=11)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon'


class OcCouponCategory(models.Model):
    coupon_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_category'
        unique_together = (('coupon_id', 'category_id'),)


class OcCouponHistory(models.Model):
    coupon_history_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_history'


class OcCouponProduct(models.Model):
    coupon_product_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_product'


class OcCourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    teacher_id = models.IntegerField()
    name = models.CharField(max_length=255)
    category_id = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=255)
    course_video = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    status = models.IntegerField()
    course_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    course_type = models.IntegerField(blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_course'


class OcCourseCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    category_type = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_course_category'


class OcCourseCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    category_descriptiontop = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_course_category_description'
        unique_together = (('category_id', 'language_id'),)


class OcCourseCategoryPath(models.Model):
    category_id = models.IntegerField(primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_course_category_path'
        unique_together = (('category_id', 'path_id'),)


class OcCourseChapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    chapter_video = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_course_chapter'


class OcCourseChapterDescription(models.Model):
    chapter_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_course_chapter_description'


class OcCourseChapterExercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    chapter_id = models.IntegerField()
    title = models.CharField(max_length=255)
    question = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    explanation = models.TextField()
    answer = models.IntegerField()
    is_quiz = models.IntegerField()
    image = models.TextField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_course_chapter_exercise'


class OcCourseDescription(models.Model):
    course_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_course_description'
        unique_together = (('course_id', 'language_id'),)


class OcCourseImage(models.Model):
    course_image_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_course_image'


class OcCourseQaCategory(models.Model):
    qa_category_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_course_qa_category'


class OcCourseQaList(models.Model):
    qa_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    qa_category_id = models.IntegerField()
    title = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_course_qa_list'


class OcCourseToStudent(models.Model):
    course_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_course_to_student'


class OcCurrency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12)
    symbol_right = models.CharField(max_length=12)
    decimal_place = models.CharField(max_length=1)
    value = models.FloatField()
    status = models.IntegerField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_currency'


class OcCustomField(models.Model):
    custom_field_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    value = models.TextField()
    validation = models.CharField(max_length=255)
    location = models.CharField(max_length=7)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field'


class OcCustomFieldCustomerGroup(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_customer_group'
        unique_together = (('custom_field_id', 'customer_group_id'),)


class OcCustomFieldDescription(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_description'
        unique_together = (('custom_field_id', 'language_id'),)


class OcCustomFieldValue(models.Model):
    custom_field_value_id = models.AutoField(primary_key=True)
    custom_field_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value'


class OcCustomFieldValueDescription(models.Model):
    custom_field_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value_description'
        unique_together = (('custom_field_value_id', 'language_id'),)


class OcCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_group_id = models.IntegerField()
    store_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.TextField()
    code = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer'


class OcCustomerActivity(models.Model):
    customer_activity_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_activity'


class OcCustomerCourse(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    paid = models.IntegerField(blank=True, null=True)
    customer_course_id = models.AutoField(primary_key=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_customer_course'


class OcCustomerCourseCategory(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    course_category_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    paid = models.IntegerField(blank=True, null=True)
    customer_course_category_id = models.AutoField(primary_key=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_customer_course_category'


class OcCustomerGroup(models.Model):
    customer_group_id = models.AutoField(primary_key=True)
    approval = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group'


class OcCustomerGroupDescription(models.Model):
    customer_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group_description'
        unique_together = (('customer_group_id', 'language_id'),)


class OcCustomerHistory(models.Model):
    customer_history_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_history'


class OcCustomerIp(models.Model):
    customer_ip_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_ip'


class OcCustomerLogin(models.Model):
    customer_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_login'


class OcCustomerOnline(models.Model):
    ip = models.CharField(primary_key=True, max_length=40)
    customer_id = models.IntegerField()
    url = models.TextField()
    referer = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_online'


class OcCustomerReward(models.Model):
    customer_reward_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward'


class OcCustomerTransaction(models.Model):
    customer_transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_transaction'


class OcCustomerWishlist(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_wishlist'
        unique_together = (('customer_id', 'product_id'),)


class OcDownload(models.Model):
    download_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=160)
    mask = models.CharField(max_length=128)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_download'


class OcDownloadDescription(models.Model):
    download_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_download_description'
        unique_together = (('download_id', 'language_id'),)


class OcEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    trigger = models.TextField()
    action = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_event'


class OcExerciseResults(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    chapter_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_exercise_results'


class OcExtension(models.Model):
    extension_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_extension'


class OcFilter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter'


class OcFilterDescription(models.Model):
    filter_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_description'
        unique_together = (('filter_id', 'language_id'),)


class OcFilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter_group'


class OcFilterGroupDescription(models.Model):
    filter_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_group_description'
        unique_together = (('filter_group_id', 'language_id'),)


class OcGeoZone(models.Model):
    geo_zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_geo_zone'


class OcGrants(models.Model):
    grant_id = models.AutoField(primary_key=True)
    date_start = models.DateField()
    date_stop = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_grants'


class OcGrantsApplication(models.Model):
    apply_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    grant_id = models.IntegerField()
    education = models.CharField(max_length=64)
    reason = models.TextField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_grants_application'


class OcGrantsDescription(models.Model):
    grant_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=255)
    information = models.TextField()
    condition = models.TextField()
    benefits = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_grants_description'


class OcHotCourses(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_hot_courses'


class OcInformation(models.Model):
    information_id = models.AutoField(primary_key=True)
    bottom = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information'


class OcInformationDescription(models.Model):
    information_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_information_description'
        unique_together = (('information_id', 'language_id'),)


class OcInformationToLayout(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_layout'
        unique_together = (('information_id', 'store_id'),)


class OcInformationToStore(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_store'
        unique_together = (('information_id', 'store_id'),)


class OcLanguage(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=5)
    locale = models.CharField(max_length=255)
    image = models.CharField(max_length=64)
    directory = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_language'


class OcLayout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout'


class OcLayoutModule(models.Model):
    layout_module_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    code = models.CharField(max_length=64)
    position = models.CharField(max_length=14)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_layout_module'


class OcLayoutRoute(models.Model):
    layout_route_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    store_id = models.IntegerField()
    route = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_layout_route'


class OcLengthClass(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'oc_length_class'


class OcLengthClassDescription(models.Model):
    length_class_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_length_class_description'
        unique_together = (('length_class_id', 'language_id'),)


class OcLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.TextField()
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    geocode = models.CharField(max_length=32)
    image = models.CharField(max_length=255, blank=True, null=True)
    open = models.TextField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_location'


class OcManufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer'


class OcManufacturerToStore(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer_to_store'
        unique_together = (('manufacturer_id', 'store_id'),)


class OcMarketing(models.Model):
    marketing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=64)
    clicks = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_marketing'


class OcMegamenu(models.Model):
    megamenu_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    is_group = models.SmallIntegerField()
    width = models.CharField(max_length=255, blank=True, null=True)
    submenu_width = models.CharField(max_length=255, blank=True, null=True)
    colum_width = models.CharField(max_length=255, blank=True, null=True)
    submenu_colum_width = models.CharField(max_length=255, blank=True, null=True)
    item = models.CharField(max_length=255, blank=True, null=True)
    colums = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    is_content = models.SmallIntegerField()
    show_title = models.SmallIntegerField()
    type_submenu = models.CharField(max_length=10)
    level_depth = models.SmallIntegerField()
    published = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    position = models.IntegerField()
    show_sub = models.SmallIntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=25, blank=True, null=True)
    privacy = models.SmallIntegerField()
    position_type = models.CharField(max_length=25, blank=True, null=True)
    menu_class = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content_text = models.TextField(blank=True, null=True)
    submenu_content = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    left = models.IntegerField()
    right = models.IntegerField()
    widget_id = models.IntegerField(blank=True, null=True)
    badges = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_megamenu'


class OcMegamenuDescription(models.Model):
    megamenu_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_megamenu_description'
        unique_together = (('megamenu_id', 'language_id'),)


class OcMegamenuWidgets(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=255)
    params = models.TextField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_megamenu_widgets'


class OcModification(models.Model):
    modification_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    link = models.CharField(max_length=255)
    xml = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_modification'


class OcModule(models.Model):
    module_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    setting = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_module'


class OcOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option'


class OcOptionDescription(models.Model):
    option_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_description'
        unique_together = (('option_id', 'language_id'),)


class OcOptionValue(models.Model):
    option_value_id = models.AutoField(primary_key=True)
    option_id = models.IntegerField()
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option_value'


class OcOptionValueDescription(models.Model):
    option_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    option_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_value_description'
        unique_together = (('option_value_id', 'language_id'),)


class OcOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    custom_field = models.TextField()
    payment_firstname = models.CharField(max_length=32)
    payment_lastname = models.CharField(max_length=32)
    payment_company = models.CharField(max_length=40)
    payment_address_1 = models.CharField(max_length=128)
    payment_address_2 = models.CharField(max_length=128)
    payment_city = models.CharField(max_length=128)
    payment_postcode = models.CharField(max_length=10)
    payment_country = models.CharField(max_length=128)
    payment_country_id = models.IntegerField()
    payment_zone = models.CharField(max_length=128)
    payment_zone_id = models.IntegerField()
    payment_address_format = models.TextField()
    payment_custom_field = models.TextField()
    payment_method = models.CharField(max_length=128)
    payment_code = models.CharField(max_length=128)
    shipping_firstname = models.CharField(max_length=32)
    shipping_lastname = models.CharField(max_length=32)
    shipping_company = models.CharField(max_length=40)
    shipping_address_1 = models.CharField(max_length=128)
    shipping_address_2 = models.CharField(max_length=128)
    shipping_city = models.CharField(max_length=128)
    shipping_postcode = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=128)
    shipping_country_id = models.IntegerField()
    shipping_zone = models.CharField(max_length=128)
    shipping_zone_id = models.IntegerField()
    shipping_address_format = models.TextField()
    shipping_custom_field = models.TextField()
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    comment = models.TextField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    order_status_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    marketing_id = models.IntegerField()
    tracking = models.CharField(max_length=64)
    language_id = models.IntegerField()
    currency_id = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=8)
    ip = models.CharField(max_length=40)
    forwarded_ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order'


class OcOrderCustomField(models.Model):
    order_custom_field_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)
    location = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'oc_order_custom_field'


class OcOrderHistory(models.Model):
    order_history_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_history'


class OcOrderOption(models.Model):
    order_option_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_product_id = models.IntegerField()
    product_option_id = models.IntegerField()
    product_option_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_option'


class OcOrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_product'


class OcOrderRecurring(models.Model):
    order_recurring_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    recurring_id = models.IntegerField()
    recurring_name = models.CharField(max_length=255)
    recurring_description = models.CharField(max_length=255)
    recurring_frequency = models.CharField(max_length=25)
    recurring_cycle = models.SmallIntegerField()
    recurring_duration = models.SmallIntegerField()
    recurring_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial = models.IntegerField()
    trial_frequency = models.CharField(max_length=25)
    trial_cycle = models.SmallIntegerField()
    trial_duration = models.SmallIntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring'


class OcOrderRecurringTransaction(models.Model):
    order_recurring_transaction_id = models.AutoField(primary_key=True)
    order_recurring_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring_transaction'


class OcOrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_status'
        unique_together = (('order_status_id', 'language_id'),)


class OcOrderTotal(models.Model):
    order_total_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_total'


class OcOrderVoucher(models.Model):
    order_voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_order_voucher'


class OcPavblogBlog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    position = models.IntegerField()
    created = models.DateField()
    status = models.IntegerField()
    user_id = models.IntegerField()
    hits = models.IntegerField()
    image = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    date_modified = models.DateField()
    video_code = models.CharField(max_length=255)
    params = models.TextField()
    tags = models.CharField(max_length=255)
    featured = models.IntegerField()
    keyword = models.CharField(max_length=255)
    banner = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavblog_blog'


class OcPavblogBlogDescription(models.Model):
    blog_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_pavblog_blog_description'


class OcPavblogCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    is_group = models.SmallIntegerField()
    width = models.CharField(max_length=255, blank=True, null=True)
    submenu_width = models.CharField(max_length=255, blank=True, null=True)
    colum_width = models.CharField(max_length=255, blank=True, null=True)
    submenu_colum_width = models.CharField(max_length=255, blank=True, null=True)
    item = models.CharField(max_length=255, blank=True, null=True)
    colums = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    is_content = models.SmallIntegerField()
    show_title = models.SmallIntegerField()
    meta_keyword = models.CharField(max_length=255)
    level_depth = models.SmallIntegerField()
    published = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    position = models.IntegerField()
    show_sub = models.SmallIntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=25, blank=True, null=True)
    privacy = models.SmallIntegerField()
    position_type = models.CharField(max_length=25, blank=True, null=True)
    menu_class = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField()
    left = models.IntegerField()
    right = models.IntegerField()
    keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_pavblog_category'


class OcPavblogCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_pavblog_category_description'
        unique_together = (('category_id', 'language_id'),)


class OcPavblogComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    blog_id = models.IntegerField()
    comment = models.TextField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_pavblog_comment'


class OcPavnewsletterDraft(models.Model):
    draft_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField(blank=True, null=True)
    to = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    affiliate = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavnewsletter_draft'


class OcPavnewsletterEmail(models.Model):
    email_id = models.AutoField(primary_key=True)
    template_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    attach = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    affiliate = models.CharField(max_length=255, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    defined = models.CharField(max_length=255, blank=True, null=True)
    special = models.CharField(max_length=255, blank=True, null=True)
    latest = models.CharField(max_length=255, blank=True, null=True)
    popular = models.CharField(max_length=255, blank=True, null=True)
    defined_categories = models.CharField(max_length=255, blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    defined_products = models.CharField(max_length=255, blank=True, null=True)
    defined_products_more = models.CharField(max_length=255, blank=True, null=True)
    only_selected_language = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    to = models.CharField(max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavnewsletter_email'


class OcPavnewsletterHistory(models.Model):
    language_id = models.IntegerField()
    template_id = models.IntegerField()
    public_id = models.IntegerField()
    store_id = models.IntegerField()
    to = models.CharField(max_length=255)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavnewsletter_history'


class OcPavnewsletterSubscribe(models.Model):
    subscribe_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavnewsletter_subscribe'


class OcPavnewsletterTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    template_file = models.CharField(max_length=200, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavnewsletter_template'


class OcPavnewsletterTemplateDescription(models.Model):
    template_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    template_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavnewsletter_template_description'


class OcPavoslidergroups(models.Model):
    title = models.CharField(max_length=255)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_pavoslidergroups'


class OcPavosliderlayers(models.Model):
    title = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    group_id = models.IntegerField()
    params = models.TextField()
    layersparams = models.TextField()
    image = models.CharField(max_length=255)
    status = models.IntegerField()
    position = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_pavosliderlayers'


class OcPavwidget(models.Model):
    pavwidget_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    setting = models.TextField()
    module_id = models.IntegerField()
    key = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_pavwidget'


class OcPaypalOrder(models.Model):
    paypal_order_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    capture_status = models.CharField(max_length=11, blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    authorization_id = models.CharField(max_length=30)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_paypal_order'


class OcPaypalOrderTransaction(models.Model):
    paypal_order_transaction_id = models.AutoField(primary_key=True)
    paypal_order_id = models.IntegerField()
    transaction_id = models.CharField(max_length=20)
    parent_id = models.CharField(max_length=20)
    date_added = models.DateTimeField()
    note = models.CharField(max_length=255)
    msgsubid = models.CharField(max_length=38)
    receipt_id = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=7, blank=True, null=True)
    payment_status = models.CharField(max_length=20)
    pending_reason = models.CharField(max_length=50)
    transaction_entity = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debug_data = models.TextField()
    call_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_paypal_order_transaction'


class OcProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    upc = models.CharField(max_length=12)
    ean = models.CharField(max_length=14)
    jan = models.CharField(max_length=13)
    isbn = models.CharField(max_length=17)
    mpn = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    quantity = models.IntegerField()
    stock_status_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField()
    shipping = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    points = models.IntegerField()
    tax_class_id = models.IntegerField()
    date_available = models.DateField()
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = models.IntegerField()
    length = models.DecimalField(max_digits=15, decimal_places=8)
    width = models.DecimalField(max_digits=15, decimal_places=8)
    height = models.DecimalField(max_digits=15, decimal_places=8)
    length_class_id = models.IntegerField()
    subtract = models.IntegerField()
    minimum = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_product'


class OcProductAttribute(models.Model):
    product_id = models.IntegerField(primary_key=True)
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product_attribute'
        unique_together = (('product_id', 'attribute_id', 'language_id'),)


class OcProductDescription(models.Model):
    product_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_product_description'
        unique_together = (('product_id', 'language_id'),)


class OcProductDiscount(models.Model):
    product_discount_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    quantity = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_product_discount'


class OcProductFilter(models.Model):
    product_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_filter'
        unique_together = (('product_id', 'filter_id'),)


class OcProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_image'


class OcProductOption(models.Model):
    product_option_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    value = models.TextField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_option'


class OcProductOptionValue(models.Model):
    product_option_value_id = models.AutoField(primary_key=True)
    product_option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()
    quantity = models.IntegerField()
    subtract = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)
    points = models.IntegerField()
    points_prefix = models.CharField(max_length=1)
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'oc_product_option_value'


class OcProductRecurring(models.Model):
    product_id = models.IntegerField(primary_key=True)
    recurring_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_recurring'
        unique_together = (('product_id', 'recurring_id', 'customer_group_id'),)


class OcProductRelated(models.Model):
    product_id = models.IntegerField(primary_key=True)
    related_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_related'
        unique_together = (('product_id', 'related_id'),)


class OcProductReward(models.Model):
    product_reward_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_reward'


class OcProductSpecial(models.Model):
    product_special_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_product_special'


class OcProductToCategory(models.Model):
    product_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_category'
        unique_together = (('product_id', 'category_id'),)


class OcProductToDownload(models.Model):
    product_id = models.IntegerField(primary_key=True)
    download_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_download'
        unique_together = (('product_id', 'download_id'),)


class OcProductToLayout(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_layout'
        unique_together = (('product_id', 'store_id'),)


class OcProductToStore(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_store'
        unique_together = (('product_id', 'store_id'),)


class OcQuizResult(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_quiz_result'


class OcRecCourses(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_rec_courses'


class OcRecurring(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    frequency = models.CharField(max_length=10)
    duration = models.IntegerField()
    cycle = models.IntegerField()
    trial_status = models.IntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial_frequency = models.CharField(max_length=10)
    trial_duration = models.IntegerField()
    trial_cycle = models.IntegerField()
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_recurring'


class OcRecurringDescription(models.Model):
    recurring_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_recurring_description'
        unique_together = (('recurring_id', 'language_id'),)


class OcResume(models.Model):
    resume_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    service_id = models.IntegerField()
    coverletter = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    coverletter_file = models.CharField(max_length=255)
    resume_file = models.CharField(max_length=255)
    response = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_resume'


class OcReturn(models.Model):
    return_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    product = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    opened = models.IntegerField()
    return_reason_id = models.IntegerField()
    return_action_id = models.IntegerField()
    return_status_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_ordered = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_return'


class OcReturnAction(models.Model):
    return_action_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_return_action'
        unique_together = (('return_action_id', 'language_id'),)


class OcReturnHistory(models.Model):
    return_history_id = models.AutoField(primary_key=True)
    return_id = models.IntegerField()
    return_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_return_history'


class OcReturnReason(models.Model):
    return_reason_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_return_reason'
        unique_together = (('return_reason_id', 'language_id'),)


class OcReturnStatus(models.Model):
    return_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_return_status'
        unique_together = (('return_status_id', 'language_id'),)


class OcReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_review'


class OcScholarship(models.Model):
    scholarship_id = models.AutoField(primary_key=True)
    date_start = models.DateField()
    date_stop = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_scholarship'


class OcScholarshipApplication(models.Model):
    apply_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    scholarship_id = models.IntegerField()
    education = models.CharField(max_length=64)
    reason = models.TextField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_scholarship_application'


class OcScholarshipDescription(models.Model):
    scholarship_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=255)
    information = models.TextField()
    condition = models.TextField()
    benefits = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_scholarship_description'


class OcService(models.Model):
    service_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_service'


class OcServiceCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    sub = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_service_category'


class OcServiceCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_service_category_description'
        unique_together = (('category_id', 'language_id'),)


class OcServiceCategoryPath(models.Model):
    category_id = models.IntegerField(primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_service_category_path'
        unique_together = (('category_id', 'path_id'),)


class OcServiceDescription(models.Model):
    service_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_service_description'
        unique_together = (('service_id', 'language_id'),)


class OcServiceImage(models.Model):
    service_image_id = models.AutoField(primary_key=True)
    service_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_service_image'


class OcServiceToCategory(models.Model):
    service_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_service_to_category'
        unique_together = (('service_id', 'category_id'),)


class OcSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    code = models.CharField(max_length=32)
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_setting'


class OcStockStatus(models.Model):
    stock_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_stock_status'
        unique_together = (('stock_status_id', 'language_id'),)


class OcStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    ssl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_store'


class OcTaxClass(models.Model):
    tax_class_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_class'


class OcTaxRate(models.Model):
    tax_rate_id = models.AutoField(primary_key=True)
    geo_zone_id = models.IntegerField()
    name = models.CharField(max_length=32)
    rate = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField(max_length=1)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate'


class OcTaxRateToCustomerGroup(models.Model):
    tax_rate_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate_to_customer_group'
        unique_together = (('tax_rate_id', 'customer_group_id'),)


class OcTaxRule(models.Model):
    tax_rule_id = models.AutoField(primary_key=True)
    tax_class_id = models.IntegerField()
    tax_rate_id = models.IntegerField()
    based = models.CharField(max_length=10)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rule'


class OcTestResults(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    chapter_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_test_results'


class OcTraining(models.Model):
    training_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    video = models.CharField(max_length=1024)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_training'


class OcTrainingCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    sub = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_training_category'


class OcTrainingCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_training_category_description'
        unique_together = (('category_id', 'language_id'),)


class OcTrainingCategoryPath(models.Model):
    category_id = models.IntegerField(primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_training_category_path'
        unique_together = (('category_id', 'path_id'),)


class OcTrainingDescription(models.Model):
    training_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_training_description'
        unique_together = (('training_id', 'language_id'),)


class OcTrainingImage(models.Model):
    training_image_id = models.AutoField(primary_key=True)
    training_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_training_image'


class OcUpload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_upload'


class OcUrlAlias(models.Model):
    url_alias_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_url_alias'


class OcUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_group_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    image = models.CharField(max_length=255)
    code = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_user'


class OcUserGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    permission = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_user_group'


class OcVoucher(models.Model):
    voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher'


class OcVoucherHistory(models.Model):
    voucher_history_id = models.AutoField(primary_key=True)
    voucher_id = models.IntegerField()
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher_history'


class OcVoucherTheme(models.Model):
    voucher_theme_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme'


class OcVoucherThemeDescription(models.Model):
    voucher_theme_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme_description'
        unique_together = (('voucher_theme_id', 'language_id'),)


class OcWeightClass(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'oc_weight_class'


class OcWeightClassDescription(models.Model):
    weight_class_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_weight_class_description'
        unique_together = (('weight_class_id', 'language_id'),)


class OcZone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_zone'


class OcZoneToGeoZone(models.Model):
    zone_to_geo_zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    geo_zone_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_zone_to_geo_zone'
