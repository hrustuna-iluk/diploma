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
        var studentMother = {},
            studentFather = {},
            fatherData = {
                fullName: this.$("#fatherFullName").val(),
                position: this.$("#fatherPosition").val(),
                phone: this.$("#fatherPhone").val()
            },
            motherData = {
                fullName: this.$("#motherFullName").val(),
                position: this.$("#motherPosition").val(),
                phone: this.$("#motherPhone").val()
            };
        if (this.studentModel.get('father')) {
            studentFather.id = this.studentModel.get('father').id;
            studentFather.fullName = fatherData.fullName;
            studentFather.position = fatherData.position;
            studentFather.phone = fatherData.phone;
        } else {
            studentFather = new FatherModel(fatherData);
        }
        if (this.studentModel.get('mother')) {
            studentMother.id = this.studentModel.get('mother').id;
            studentMother.fullName = motherData.fullName;
            studentMother.position = motherData.position;
            studentMother.phone = motherData.phone;
        } else {
            studentMother = new MotherModel(motherData);
        }

        this.studentModel.set({
           mother: studentMother,
           father: studentFather
        });
        this._cancelModalWindow();
    },

    _fillFields: function () {
        if (this.studentModel.get('father')) {
            this.$("#fatherFullName").val(this.studentModel.get('father').fullName);
            this.$("#fatherPosition").val(this.studentModel.get('father').position);
            this.$("#fatherPhone").val(this.studentModel.get('father').phone);
        }
        if (this.studentModel.get('mother')) {
            this.$("#motherFullName").val(this.studentModel.get('mother').fullName);
            this.$("#motherPosition").val(this.studentModel.get('mother').position);
            this.$("#motherPhone").val(this.studentModel.get('mother').phone);
        }


    },

    _cancelModalWindow: function() {
        this.remove();
        $('body').removeClass('modal-open');
        $('.modal-backdrop').hide();
    },

    render: function() {
        this.$el = $(this.template());
        this._fillFields();
        this.$el.modal('show');
        this._attachEvents();
        return this;
    }

});