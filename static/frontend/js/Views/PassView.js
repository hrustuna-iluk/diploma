var PassView = BaseView.extend ({

    PASS_TYPES: {
        pass: 'Без поважної причини',
        sickness: 'По хворобі',
        statement: 'Заява',
        watch: 'Чергування'
    },

    popoverTemplate: _.template(
        '<select class="pass_type" style="color: black;">' +
            '<option value="" disabled selected>Виберіть причину пропуску</option>' +
            '<% _.each(pass_types, function(value, key) { %>' +
                '<option value="<%=key %>"><%=value%></option>' +
            '<% }); %>' +
        '</select>'
    ),

    className: 'pass',

    initialize: function(options) {
        this.student = options.student;
        this.class = options.class;
        this.date = options.date;
        this.model = options.model;
        this.passesCollection = options.passesCollection;
    },

    events: {
        'click': '_onClick'
    },

    _initWidgets: function () {
            this.$el.popover({
            html: true,
            placement: 'left',
            content: this.popoverTemplate({
                pass_types: this.PASS_TYPES
            }),
            container: this.$el,
            trigger: 'click'
        });
        this.$el.on('change', '.pass_type', $.proxy(this._passTypeChanged, this));
        this.$el.on('click', '.pass_type', $.proxy(function () {
            $('.popover').addClass('in');
            return false;
        }, this));
    },

    _attachEvents: function() {},

    _onClick: function() {
        $('.popover').not(this.$el.find('.popover')).popover('hide');
    },

    _passTypeChanged: function (evt) {
        var type = $(evt.target).val();
        this.model = this.model || new PassModel();
        this.model.set({
            student: this.student,
            class_passed: this.class,
            date: this.date.toISOString().split('T')[0],
            type: type
        }).save({}, {
            success: $.proxy(this._savedPass, this)
        });
        $('.popover').popover('hide');
        return false;
    },

    _savedPass: function (model) {
        this.passesCollection.add(model);
        if (this.model.get('type') == 'pass') {
            this.$el.css({color: 'red'});
        } else {
            this.$el.css({color: 'white'});
        }
        this.$el.text('Н');
    },

    render: function() {
        if (this.model) {
            if (this.model.get('type') == 'pass') {
                this.$el.css({color: 'red'});
            } else {
                this.$el.css({color: 'white'});
            }
            this.$el.text('Н');
        }
        this._initWidgets();
        this._attachEvents();
        return this;
    }
});