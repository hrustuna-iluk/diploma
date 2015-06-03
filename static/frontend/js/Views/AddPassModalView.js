var AddPassModalView = BaseView.extend({
    selectors: {
        add: '.addPass',
        addPassForm: '.addPassForm',
        close: '.closeModal'
    },

    template: _.template($('#addPassModalTemplate').html()),

    events: function () {
        return _.invert({
            '_add': 'click ' + this.selectors.add
        });
    },

    initialize: function (options) {
        this.studentsCollection = options.studentsCollection;
        this.classesCollection = options.classesCollection;
    },

    _add: function () {
        var form = this.$(this.selectors.addPassForm).get(0).elements;
        var data = {};
        for (var i = 0; i < form.length; i++) {
            data[form[i].name] = form[i].value;
        }
        new PassModel(data).save({}, {
            success: function () {
                alert('Додано');
            }
        });
        this.hide();
    },

    _renderFields: function () {
        this.classesCollection.reduce($.proxy(function ($el, classItem) {
            var option = new Option();
            option.value = classItem.get('id');
            option.innerText = classItem.get('subject');
            return $el.add(option);
        }, this), $()).appendTo(this.$(this.selectors.addPassForm).find('.class_passed'));

        this.studentsCollection.reduce($.proxy(function ($el, student) {
            var option = new Option();
            option.value = student.get('id');
            option.innerText = [student.get('lastName'), student.get('firstName')].join(' ');
            return $el.add(option);
        }, this), $()).appendTo(this.$(this.selectors.addPassForm).find('.student'));
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
