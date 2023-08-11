from django.contrib.contenttypes.models import ContentType
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):

    def _init_components(self):

        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first_name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last_name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last_login',
            name='last_login',
            anchor='100%',
            format='d.m.Y')

        self.field__date_joined = ext.ExtDateField(
            label=u'date_joined',
            name='date_joined',
            anchor='100%',
            format='d.m.Y')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'is_superuser',
            name='is_superuser',
            anchor='100%',
            checked=False)

        self.field__is_staff = ext.ExtCheckBox(
            label=u'is_staff',
            name='is_staff',
            anchor='100%',
            checked=False)

        self.field__is_active = ext.ExtCheckBox(
            label=u'is_active',
            name='is_active',
            anchor='100%',
            checked=True
        )

    def _do_layout(self):

        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__last_login,
            self.field__date_joined,
            self.field__is_superuser,
            self.field__is_staff,
            self.field__is_active,
        ))

    def set_params(self, params):

        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):

        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = make_combo_box(
            label=u'content_type',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=[(i.id, i.name) for i in ContentType.objects.all()]
        )

        self.field__code_name = ext.ExtStringField(
            label=u'code_name',
            name='code_name',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):

        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__code_name,
        ))

    def set_params(self, params):

        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'
