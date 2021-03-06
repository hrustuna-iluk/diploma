var AdminUserAccessView = BaseView.extend({

    template: _.template($("#adminUserAccessTemplate").html()),

    optionStudentUserTemplate: _.template('<option data-id="<%=id%>" value="<%=lastName%> <%=firstName%> <%=middleName%> <<%=email%>>">'),

    optionTeacherUserTemplate: _.template('<option data-id="<%=id%>" value="<%=lastName%> <%=firstName%> <%=middleName%> <<%=email%>>">'),

    initialize: function(options) {
        this.studentsCollection = options.studentsCollection;
        this.teachersCollection = options.teachersCollection;
        this.groupsCollection = options.groupsCollection;
    },

    _attachEvents: function() {
        this.$('#addTeacherUser').on('click', $.proxy(this._addTeacherUser, this));
        this.$('#addStudentUser').on('click', $.proxy(this._addStudentUser, this));
        this.$('[name=studentUserSelect]').on('change input', $.proxy(this._fillStudentUserData, this));
        this.$('[name=teacherUserSelect]').on('change input', $.proxy(this._fillTeacherUserData, this));
    },

    _fillStudentUserData: function (evt) {
        var value = this.$('[name=studentUserSelect]').val();
        var studentId = this.$('#studentUserSelect').find('[value="' + value + '"]').data('id');
        this.$('#studentUserLogin').val('');
        if (!studentId) return;

        var student = this.studentsCollection.findWhere({ id: studentId });
        if (student.get('user')) {
            this.$('#studentUserLogin').val(student.get('user').username);
        }
    },

    _fillTeacherUserData: function (evt) {
        var value = this.$('[name=teacherUserSelect]').val();
        var teacherId = this.$('#teacherUserSelect').find('[value="' + value + '"]').data('id');
        this.$('#teacherUserLogin').val('');
        if (!teacherId) return;

        var teacher = this.teachersCollection.findWhere({ id: teacherId });
        if (teacher.get('user')) {
            this.$('#teacherUserLogin').val(teacher.get('user').username);
        }
    },

    _addTeacherUser: function() {
        var value = this.$('[name=teacherUserSelect]').val();
        var teacherId = this.$('#teacherUserSelect').find('[value="' + value + '"]').data('id');
        var userModel = new UserModel();
        if (!teacherId) {
            alert('Виберіть спочатку викладача');
            return;
        }
        var teacher = this.teachersCollection.findWhere({ id: teacherId });

       /* if (teacher.get('position') == 'teacher' && !this.groupsCollection.filter(function (group) {
            return group.get('curator') && group.get('curator').id == teacherId;
        }).length) {
            alert('Отримати доступ має можливість лише декан, завідувач кафедри, заступник декана та куратор.');
            return;
        }*/
        if (_.isObject(teacher.get('user'))) {
            userModel.set(teacher.get('user'));
        }
        userModel.set({
            username: this.$('#teacherUserLogin').val(),
            password: this.$('#teacherUserPassword').val()
        });

        teacher.set({
            user: userModel
        });

        teacher.save({}, {
            success: $.proxy(function () {
                    this._renderTeachersUser();
            }, this)
        });
        this.$('#teacherUserSelect').val('');
        this.$('#teacherUserLogin').val('');
        this.$('#teacherUserPassword').val('');
    },

    _addStudentUser: function() {
        var value = this.$('[name=studentUserSelect]').val();
        var studentId = this.$('#studentUserSelect').find('[value="' + value + '"]').data('id');
        var userModel = new UserModel();
        if (!studentId) {
            alert('Виберіть спочатку студента');
            return;
        }
        var student = this.studentsCollection.findWhere({ id: studentId });

        if (!this.groupsCollection.filter(function (group) {
            return group.get('leader') && group.get('leader').id == studentId;
        }).length) {
            alert('Отримати доступ має можливість лише староста групи.');
            return;
        }
        if (_.isObject(student.get('user'))) {
            userModel.set(student.get('user'));
        }

        userModel.set({
            username: this.$('#studentUserLogin').val(),
            password: this.$('#studentUserPassword').val()
        });
        student.set({
            user: userModel
        });
        student.save({}, {
            success: $.proxy(function () {
                    this._renderStudentUser();
            }, this)
        });
        this.$('#studentUserSelect').val('');
        this.$('#studentUserLogin').val('');
        this.$('#studentUserPassword').val('');
    },

    _renderTeachersUser: function() {
        this.$("#userTeacherTable table tbody").empty();
        this.teachersCollection.each($.proxy(function (model, index) {
            if (!model.get('user')) return;
            this.$("#userTeacherTable table tbody").append(
                new UserTableView({
                    model: model,
                    index: index + 1
                }).render().el
            );
        }, this));
    },

    _renderStudentUser: function () {
        this.$("#userStudentTable table tbody").empty();
        this.studentsCollection.chain().filter(function (model) {
            return model.get('user');
        }).each($.proxy(function (model, index) {
            this.$("#userStudentTable table tbody").append(
                new UserTableView({
                    model: model,
                    index: index + 1
                }).render().el
            );
        }, this));
    },

    _fillTeacherUserList: function() {
        this.teachersCollection.each(function(model) {
            this.$('#teacherUserSelect').append(this.optionTeacherUserTemplate(model.toJSON()));
        }, this);
    },

    _fillStudentUserList: function() {
        this.studentsCollection.each(function(model) {
            this.$('#studentUserSelect').append(this.optionStudentUserTemplate(model.toJSON()));
        }, this);
    },

    render: function() {
        this.$el.html(this.template);
        this._fillStudentUserList();
        this._fillTeacherUserList();
        this._attachEvents();
        this._renderStudentUser();
        this._renderTeachersUser();
        return this;
    }

});