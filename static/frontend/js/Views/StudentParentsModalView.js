var StudentParentsModalView = BaseView.extend({

    template: _.template($("#studentParentsModalTemplate").html()),

    initialize: function(options) {
        this.studentModel = options.studentModel;
    },

    _attachEvents: function() {
        this.$('.addParents').on('click', $.proxy(this._addParents, this));
        this.$('.closeModal').on('click', $.proxy(this._cancelModalWindow, this));
    },

    _addParents: function() {
        var studentMother = new MotherModel({
                fullName: this.$("#motherFullName").val(),
                position: this.$("#motherPosition").val(),
                phone: this.$("#motherPhone").val()
            }),
            studentFather = new FatherModel({
                fullName: this.$("#fatherFullName").val(),
                position: this.$("#fatherPosition").val(),
                phone: this.$("#fatherPhone").val()
            })
        this.studentModel.set({
           mother: studentMother,
           father: studentFather
        });
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