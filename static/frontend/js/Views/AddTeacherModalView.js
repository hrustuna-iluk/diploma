var AddTeacherModalView = BaseView.extend({

    template: _.template($("#addTeacherModalTemplate").html()),

    initialize: function(options) {
        this.department = options.department;
    },

    _attachEvents: function() {
        this.$('.addTeacher').on('click', $.proxy(this._addCurator, this));
        this.$('.closeModal').on('click', $.proxy(this._cancelModalWindow, this));
    },

    _addTeacher: function() {
        var teacher = new TeacherModel({
                        name: this.$("#teacherName").val(),
                        surname: this.$("#teacherSurname").val(),
                        middleName: this.$("#teacherMiddleName").val(),
                        position: this.$("#teacherPosition").val(),
                        department: this.department
                        })
            //teacher.save();
        this._cancelModalWindow();
    },

    _cancelModalWindow: function() {
        this.remove();
        $('body').removeClass('modal-open');
        $('.modal-backdrop').hide();
    },

    render: function() {
        this.$el = $(this.template());
        this.$el.modal('show');
        this._attachEvents();
        return this;
    }

});