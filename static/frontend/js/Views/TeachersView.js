var TeachersView = BaseView.extend({

    template: _.template($("#teachersTemplate").html()),

    collectionLen: 0,

    selectors: {
        createTeacher: "#addTeacher",
        changeTeacherData: "#changeTeacherData",
        teacherNameInput: "#teacherName",
        teacherSurnameInput: "#teacherSurname",
        teacherMiddleNameInput: "#teacherMiddleName",
        teacherPositionSelect: "#teacherPosition",
        teacherPhone: "#teacherPhone",
        teacherEmail: "#teacherEmail"
    },

    initialize: function(options) {
        this.collection = options.collection;
        this.faculty = options.faculty;
        this.department = options.department;
        this.collection.on("add", $.proxy(this._renderTeacher, this));
        this.publisher.on('change:teacher', $.proxy(this._onTeacherChange, this));
        this.collection.reset().fetch({data: {
            department: this.department.get('id')
        }, processData: true});
    },

    _attachEvents: function() {
        this.$(this.selectors.createTeacher).on('click', $.proxy(this._addTeacher, this));
        this.$(this.selectors.changeTeacherData).on('click', $.proxy(this._changeTeacherData, this));
    },

    _onTeacherChange: function(model) {
        $(this.selectors.teacherSurnameInput).val(model.getSurname());
        $(this.selectors.teacherNameInput).val(model.getName());
        $(this.selectors.teacherMiddleNameInput).val(model.getMiddleName());
        $(this.selectors.teacherPhone).val(model.getPhone());
        $(this.selectors.teacherEmail).val(model.getEmail());
        this.$(this.selectors.changeTeacherData).data('model', model);
        this.$(this.selectors.createTeacher).addClass('no-display');
        this.$(this.selectors.changeTeacherData).removeClass('no-display');
    },

    _teacherData: function(teacherModel) {
        teacherModel.setSurname(this.$(this.selectors.teacherSurnameInput).val());
        teacherModel.setName(this.$(this.selectors.teacherNameInput).val());
        teacherModel.setMiddleName(this.$(this.selectors.teacherMiddleNameInput).val());
        teacherModel.setPosition(this.$(this.selectors.teacherPositionSelect).val());
        teacherModel.setPhone(this.$(this.selectors.teacherPhone).val());
        teacherModel.setEmail(this.$(this.selectors.teacherEmail).val());
        teacherModel.set('department', this.department);
        this.$(this.selectors.teacherPhone).val('');
        this.$(this.selectors.teacherEmail).val('');
        this.$(this.selectors.teacherSurnameInput).val("");
        this.$(this.selectors.teacherNameInput).val("");
        this.$(this.selectors.teacherMiddleNameInput).val("");
        this.$(this.selectors.teacherPositionSelect).find('option:first').attr('selected', true);
    },

    _addTeacher: function() {
        var model = new TeacherModel();
        this._teacherData(model);
        model.save({wait: true}, {success: $.proxy(function() {
            this.collection.add(model);
            if(model.getPosition() === 'dean') {
                this.faculty.set('dean', model);
                this.faculty.save();
            }
        }, this)});
    },

    _changeTeacherData: function() {
        var teacherModel = this.$(this.selectors.changeTeacherData).data('model');
        this._teacherData(teacherModel);
        teacherModel.save();
        this.$(this.selectors.changeTeacherData).addClass('no-display');
        this.$(this.selectors.createTeacher).removeClass('no-display');
    },

    _renderTeacher: function(model) {
        this.$("#teachers table tbody").append(
            new TeacherView({
                model: model
            }).render().el
        );

        this.$("#teachers table tbody tr:last td:first").text(++this.collectionLen);
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }
});