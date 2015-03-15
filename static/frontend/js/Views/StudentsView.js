var StudentsView = BaseView.extend({

    template: _.template($("#studentsTemplate").html()),

    optionLanguageTemplate: _.template($("#optionLanguageTemplate").html()),

    optionBenefitTemplate: _.template($("#optionBenefitsTemplate").html()),

    optionPublicOrderTemplate: _.template($("#optionPublicOrdersTemplate").html()),

    selectors: {
        createStudent: "#addStudent",
        changeStudentData: "#changeStudentData",
        studentNameInput: "#studentName",
        studentSurnameInput: "#studentSurname",
        studentMiddleNameInput: "#studentMiddleName",
        studentSexInput: '#sex',
        studentDateBirthInput: '#studentDateOfBirth',
        studentAddressInput: '#studentAddress',
        studentPhoneInput: '#studentTelephone',
        studentNationalityInput: '#studentNationality',
        studentMaritalStatusSelect: '#maritalStatus',
        studentStudyLanguageSelect: '#learnLanguage',
        studentSchoolInput: '#studentSchool',
        studentBenefitsSelect: '#studentBenefits',
        studentPublicOrdersSelect: '#publicOrders',
        isProcurement: '#isProcurement',
        studentCurrentAddress: '#currentAddress'
        //studentAdditionals

    },

    initialize: function(options) {
        this.collection = options.collection;
        this.benefitsCollection = options.benefitsCollection;
        this.languagesCollection = options.languagesCollection;
        this.publicOrdersCollection = options.publicOrdersCollection;
        this.group = options.group;
        this.collection.on("add", $.proxy(this._renderStudent, this));
        this.publisher.on('change student data', $.proxy(this._onStudentChange, this));
    },

    _attachEvents: function() {
        this.$(this.selectors.createStudent).on('click', $.proxy(this._addStudent, this));
        this.$(this.selectors.changeStudentData).on('click', $.proxy(this._changeStudentData, this));
    },

    _onStudentChange: function(model) {
        $(this.selectors.studentSurnameInput).val(model.getSurname());
        $(this.selectors.studentNameInput).val(model.getName());
        $(this.selectors.studentMiddleNameInput).val(model.getMiddleName());
        $(this.selectors.studentSexInput).val(model.getSex());
        $(this.selectors.studentDateBirthInput).val(model.getDateBirth());
        $(this.selectors.studentAddressInput).val(model.getAddress());
        $(this.selectors.studentCurrentAddress).val(model.getCurrentAddress());
        $(this.selectors.studentPhoneInput).val(model.getPhone());
        $(this.selectors.studentNationalityInput).val(model.getNationality());
        $(this.selectors.studentMaritalStatusSelect).val(model.getMaritalStatus());
        $(this.selectors.studentStudyLanguageSelect).val(model.getLanguage());
        $(this.selectors.studentSchoolInput).val(model.getSchool());
        $(this.selectors.studentBenefitsSelect).val(model.getBenefits());
        $(this.selectors.studentPublicOrdersSelect).val(model.getPublicOrders());
        $(this.selectors.isProcurement).val(model.getIsProcurement());

        this.$(this.selectors.changeStudentData).data('model', model);
        this.$(this.selectors.createStudent).addClass('no-display');
        this.$(this.selectors.changeStudentData).removeClass('no-display');
    },

    _studentData: function(studentModel) {
         studentModel.set({
            name: this.$(this.selectors.studentNameInput).val(),
            surname: this.$(this.selectors.studentSurnameInput).val(),
            middleName: this.$(this.selectors.studentMiddleNameInput).val(),
            address: this.$(this.selectors.studentAddressInput).val(),
            currentAddress: this.$(this.selectors.studentCurrentAddress).val(),
            phone: this.$(this.selectors.studentPhoneInput).val(),
            nationality: this.$(this.selectors.studentNationalityInput).val(),
            school: this.$(this.selectors.studentSchoolInput).val(),
            sex: this.$(this.selectors.studentSexInput).val(),
            dateBirth: this.$(this.selectors.studentDateBirthInput).val(),
            maritalStatus: this.$(this.selectors.studentMaritalStatusSelect).val(),
            publicOrders: this.$(this.selectors.studentPublicOrdersSelect).val(),
            benefits: this.$(this.selectors.studentBenefitsSelect).val(),
            isProcurement: this.$(this.selectors.isProcurement).val(),
            language: this.$(this.selectors.studentStudyLanguageSelect).val()
        });
        this.$(this.selectors.studentSurnameInput).val("");
        this.$(this.selectors.studentNameInput).val("");
        this.$(this.selectors.studentMiddleNameInput).val("");
        this.$(this.selectors.studentAddressInput).val("");
        this.$(this.selectors.studentCurrentAddress).val("");
        this.$(this.selectors.studentPhoneInput).val("");
        this.$(this.selectors.studentNationalityInput).val("");
        this.$(this.selectors.studentSchoolInput).val("");

    },

    _addStudent: function() {
        var studentModel = new StudentModel({
            group: this.group
        });
        this._studentData(studentModel);
        this.collection.add(studentModel);
    },

    _changeStudentData: function() {
        var studentModel = this.$(this.selectors.changeStudentData).data('model');
        this._studentData(studentModel);
        this.$(this.selectors.changeStudentData).addClass('no-display');
        this.$(this.selectors.createStudent).removeClass('no-display');
    },

    _renderStudent: function(model) {
        this.$("#students table tbody").append(
            new StudentView({
                model: model
            }).render().el
        );
    },

     _fillBenefitsList: function() {
        this.benefitsCollection.each(function(model) {
            this.$('#studentBenefits').append(this.optionBenefitTemplate(model.toJSON()));
        }, this);
    },

    _fillLanguageList: function() {
        this.languagesCollection.each(function(model) {
            this.$('#learnLanguage').append(this.optionLanguageTemplate(model.toJSON()));
        }, this);
    },

    _fillPublicOrdersList: function() {
        this.publicOrdersCollection.each(function(model) {
            this.$('#publicOrders').append(this.optionPublicOrderTemplate(model.toJSON()));
        }, this);
    },

    render: function() {
        this.$el.html(this.template);
        //this._fillBenefitsList();
        //this._fillLanguageList();
        //this._fillPublicOrdersList();
        this._attachEvents();
        return this;
    }
});