var StudentsView = BaseView.extend({

    template: _.template($("#studentsTemplate").html()),

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
        isProcurement: '#isProcurement'
        //studentAdditionals

    },

    initialize: function(options) {
        this.collection = options.collection;
        this.model = options.group;
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


        this.$(this.selectors.changeStudentData).data('model', model);
        this.$(this.selectors.createStudent).addClass('no-display');
        this.$(this.selectors.changeStudentData).removeClass('no-display');
    },

    _studentData: function(studentModel) {
        var studentSurname = this.$(this.selectors.studentSurnameInput).val(),
            studentName = this.$(this.selectors.studentNameInput).val(),
            studentMiddleName = this.$(this.selectors.studentMiddleNameInput).val();
        this.$(this.selectors.studentSurnameInput).val("");
        this.$(this.selectors.studentNameInput).val("");
        this.$(this.selectors.studentMiddleNameInput).val("");
        studentModel.setSurname(studentSurname);
        studentModel.setName(studentName);
        studentModel.setMiddleName(studentMiddleName);
    },

    _addStudent: function() {
        var studentModel = new StudentModel();
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

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }
});