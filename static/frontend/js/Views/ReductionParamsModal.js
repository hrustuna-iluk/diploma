var ReductionParamsModalView = BaseView.extend({
    selectors: {
        save: '.sendParams',
        reductionParamsForm: '.reductionParamsForm',
        close: '.closeModal'
    },

    template: _.template($('#reductionParamsTemplate').html()),
    sectionTemplate: _.template($('#reductionParamsSection').html()),

    events: function () {
        return _.invert({
            '_saveData': 'click ' + this.selectors.save
        });
    },

    initialize: function (options) {
        this.departmentsCollection = options.departmentsCollection;
    },

    _saveData: function () {
        var data = {};
        this.trigger('params', data);
    },

    _renderFields: function () {
        this.departmentsCollection.reduce($.proxy(function ($el, department) {
            return $el.add(this.sectionTemplate(department.toJSON()));
        }, this), $()).appendTo( this.$(this.selectors.reductionParamsForm) );
    },

    _fillFields: function () {

    },

    show: function () {
        this.$el.modal('show');
        return this;
    },

    hide: function () {
        this.$el.modal('hide');
        return this;
    },

    render: function () {
        this.$el = $(this.template());
        this.delegateEvents();
        this._renderFields();
        return this;
    }
});
