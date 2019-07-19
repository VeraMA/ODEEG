# generated by appcreator
from django.utils.safestring import mark_safe
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup
from . models import (
    Certainty,
    CollectionSpec,
    Culture,
    Fabric,
    Hardware,
    Illustration,
    IllustrationPanel,
    ImagingTechnique,
    Institution,
    Material,
    Object,
    PaintingStyle,
    PaintingSubTechnique,
    Period,
    Person,
    Place,
    Shape,
    ShapeComponent,
    ThreedData
)


class CertaintyFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CertaintyFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'cert_label',
                    'cert_id',
                    css_id="more"
                    )
                ),
            HTML('<hr>')
            )


class CertaintyForm(forms.ModelForm):
    class Meta:
        model = Certainty
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CertaintyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class CollectionSpecFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CollectionSpecFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'collection_spec',
                    'partof_institution',

                    css_id="more"
                    )
                ),
            HTML('<hr>')
            )


class CollectionSpecForm(forms.ModelForm):
    class Meta:
        model = CollectionSpec
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CollectionSpecForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class CultureFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CultureFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'culture',
                    'culture_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class CultureForm(forms.ModelForm):
    class Meta:
        model = Culture
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CultureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class FabricFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FabricFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'material_fabric',
                    'material_fabric_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class FabricForm(forms.ModelForm):
    class Meta:
        model = Fabric
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FabricForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class HardwareFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(HardwareFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'threed_hardware',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HardwareForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class IllustrationFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(IllustrationFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'folder_name',
                    'ill_date',
                    'ill_author',
                    'ill_software',
                    'ill_software_steps',
                    'ill_notes',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class IllustrationForm(forms.ModelForm):
    class Meta:
        model = Illustration
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(IllustrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class IllustrationPanelFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(IllustrationPanelFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'folder_name',
                    'illtab_date',
                    'illtab_author',
                    'illtab_software',
                    'illtab_software_steps',
                    'illtab_notes',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class IllustrationPanelForm(forms.ModelForm):
    class Meta:
        model = IllustrationPanel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(IllustrationPanelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ImagingTechniqueFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ImagingTechniqueFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'threed_technique',
                    'threed_technique_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class ImagingTechniqueForm(forms.ModelForm):
    class Meta:
        model = ImagingTechnique
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ImagingTechniqueForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class InstitutionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InstitutionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'inst_name',
                    'inst_geo_id',
                    'inst_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class MaterialFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(MaterialFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'material',
                    'material_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ObjectFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ObjectFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'inv_nr',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'folder_name',
                    'collection_inst',
                    'collection_spec',
                    'inv_nr',
                    'bapd_nr',
                    'shape',
                    'shape_comp',
                    'object_associated_to_inv',
                    'period',
                    'culture',
                    'material',
                    'material_fabric',
                    'painting_style',
                    'painting_style_sub',
                    'provenance_spot',
                    'provenance_spot_cert',
                    'provenance_production',
                    'provenance_production_cert',
                    'provenance_attribution',
                    'provenance_acquisition',
                    'provenance_acquisition_date',
                    'bibref',
                    'collref',
                    'weight',
                    'width',
                    'height',
                    'length',
                    'fillingheight',
                    'fillingvolume',
                    'materialvolume',
                    'materialdensity',
                    'materialdensity_measure',
                    'boundingbox',
                    # 'object_notes',
                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ObjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PaintingStyleFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PaintingStyleFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'painting_style',
                    'painting_style_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class PaintingStyleForm(forms.ModelForm):
    class Meta:
        model = PaintingStyle
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PaintingStyleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PaintingSubTechniqueFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PaintingSubTechniqueFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'painting_style_sub',
                    'painting_style_sub_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class PaintingSubTechniqueForm(forms.ModelForm):
    class Meta:
        model = PaintingSubTechnique
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PaintingSubTechniqueForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PeriodFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PeriodFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'period',
                    'period_abbrev',
                    'period_id',


                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PeriodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PersonFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PersonFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'person_last_name',
                    'person_first_name',
                    'person_member_inst',
                    'person_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PlaceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PlaceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'place_name',
                    'geonames_id',
                    'coord_exact',
                    'place_type',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ShapeFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ShapeFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'shape',
                    'shape_alt',
                    'shape_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class ShapeForm(forms.ModelForm):
    class Meta:
        model = Shape
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ShapeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ShapeComponentFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ShapeComponentFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'shape_comp',
                    'shape_comp_id',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class ShapeComponentForm(forms.ModelForm):
    class Meta:
        model = ShapeComponent
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ShapeComponentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ThreedDataFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ThreedDataFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            HTML('<hr>'),
            Accordion(
                AccordionGroup(
                    mark_safe('Advanced search <i data-feather="chevron-down"></i>'),
                    'folder_name',
                    'threed_location',
                    'threed_location_char',
                    'threed_date',
                    'threed_author',
                    'threed_technique',
                    'threed_hardware',
                    'threed_fov',
                    'threed_resolution',
                    'threed_acc',
                    'threed_texture_acquisition',
                    'threed_texture_color',
                    'threed_texture_resolution',
                    'threed_software',
                    'threed_scan_nrs',
                    'threed_merging_date',
                    'threed_merging_author',
                    'threed_merging_software',
                    'threed_postproc_date',
                    'threed_postproc_author',
                    'threed_postproc_software',
                    'threed_postproc_actions',
                    'threed_postproc_file',
                    'threed_postproc_low_date',
                    'threed_postproc_low_author',
                    'threed_postproc_low_software',
                    'threed_postproc_low_software_actions',
                    'threed_postproc_low_file',
                    'threed_notes',

                    css_id="more"
                    ),
                ),
            HTML('<hr>')
            )


class ThreedDataForm(forms.ModelForm):
    class Meta:
        model = ThreedData
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ThreedDataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)