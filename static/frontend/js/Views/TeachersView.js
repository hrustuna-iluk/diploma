var TeachersView = BaseView.extend({

    template: _.template($("#teachersTemplate").html()),

    selectors: {
        createTeacher: "#addTeacher",
        changeTeacherData: "#changeTeacherData",
        teacherNameInput: "#teacherName",
        teacherSurnameInput: "#teacherSurname",
        teacherMiddleNameInput: "#teacherMiddleName",
        teacherPositionSelect: "#teacherPosition"
    },

    initialize: function(options) {
        this.collection = options.collection;
        this.faculty = options.faculty;
        this.department = options.department;
        this.collection.on("add", $.proxy(this._renderTeacher, this));
        this.publisher.on('change:teacher', $.proxy(this._onTeacherChange, this));
        this.collection.reset().fetch({data: {
            department: this.department.get('id')
        }});
    },

    _attachEvents: function() {
        this.$(this.selectors.createTeacher).on('click', $.proxy(this._addTeacher, this));
        this.$(this.selectors.changeTeacherData).on('click', $.proxy(this._changeTeacherData, this));
    },

    _onTeacherChange: function(model) {
        $(this.selectors.teacherSurnameInput).val(model.getSurname());
        $(this.selectors.teacherNameInput).val(model.getName());
        $(this.selectors.teacherMiddleNameInput).val(model.getMiddleName());
        this.$(this.selectors.changeTeacherData).data('model', model);
        this.$(this.selectors.createTeacher).addClass('no-display');
        this.$(this.selectors.changeTeacherData).removeClass('no-display');
    },

    _teacherData: function(teacherModel) {
        var teacherSurname = this.$(this.selectors.teacherSurnameInput).val(),
            teacherName = this.$(this.selectors.teacherNameInput).val(),
            teacherMiddleName = this.$(this.selectors.teacherMiddleNameInput).val(),
            teacherPosition = this.$(this.selectors.teacherPositionSelect).val();
        this.$(this.selectors.teacherSurnameInput).val("");
        this.$(this.selectors.teacherNameInput).val("");
        this.$(this.selectors.teacherMiddleNameInput).val("");
        this.$(this.selectors.teacherPositionSelect).find('option:first').attr('selected', true);
        teacherModel.setSurname(teacherSurname);
        teacherModel.setName(teacherName);
        teacherModel.setMiddleName(teacherMiddleName);
        teacherModel.setPosition(teacherPosition);
        teacherModel.set('department', this.department);
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
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }
});