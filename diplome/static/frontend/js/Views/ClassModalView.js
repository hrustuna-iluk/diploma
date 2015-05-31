var ClassModalView = BaseView.extend({

    template:  _.template($("#classModalTemplate").html()),

    optionSelectTemplateForTeacher: _.template($("#optionTeacherTemplate").html()),

    initialize: function(options) {
        this.group = options.group;
        this.teachersCollection = options.teachersCollection;
    },

    _attachEvents: function() {
        this.$('.addClass').on('click', $.proxy(this._addClass, this));
        this.$('.closeModal').on('click', $.proxy(this._cancelModalWindow, this));
    },

    _addClass: function() {
        this.model.set ({
            subject: this.$('.subjectTitle').val(),
            type: this.$('.typeClass').val(),
            teacher: +this.$('.classTeacher').val(),
            classroom: this.$('.classNumber').val()
        });
        this.model.save();
        this.trigger('saved', this.model);
        this._cancelModalWindow();
    },

    _cancelModalWindow: function() {
        this.remove();
        $('body').removeClass('modal-open');
        $('.modal-backdrop').hide();
    },

    _fillTeachersList: function() {
         this.teachersCollection.each(function(model) {
            this.$('.classTeacher').append(this.optionSelectTemplateForTeacher(model.toJSON()));
        }, this);
    },

    render: function() {
        this.$el = $(this.template(this.model.toJSON()));
        this.$el.modal('show');
        this._fillTeachersList();
        this._attachEvents();
        return this;
    }

});