var AdminUserAccessView = BaseView.extend({

    template: _.template($("#adminUserAccessTemplate").html()),

    optionStudentUserTemplate: _.template($("#optionStudentUserTemplate").html()),

    optionTeacherUserTemplate: _.template($("#optionTeacherUserTemplate").html()),

    initialize: function(options) {
        this.studentsCollection = options.studentsCollection;
        this.teachersCollection = options.teachersCollection;
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

        teacher.save({
            success: $.proxy(function () {
                    this._renderUser(teacher);
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
        student.save({
            success: $.proxy(function () {
                    this._renderUser(student);
            }, this)
        });
        this.$('#studentUserSelect').val('');
        this.$('#studentUserLogin').val('');
        this.$('#studentUserPassword').val('');
    },

    _renderUser: function(model) {
        if (model && model.position) {
            this.$("#userTeacherTable table tbody").append(
                new UserTableView({
                    model: model
                }).render().el
            );
        } else {
            this.$("#userStudentTable table tbody").append(
                new UserTableView({
                    model: model
                }).render().el
            );
        }
    },

    _fillTeacherUserList: function() {
        this.teachersCollection.reset().fetch({
            success: $.proxy(function () {
                this.teachersCollection.each(function(model) {
                    this.$('#teacherUserSelect').append(this.optionTeacherUserTemplate(model.toJSON()));
                }, this);
        }, this)
        });
    },

    _fillStudentUserList: function() {
        this.studentsCollection.reset().fetch({
            success: $.proxy(function () {
                this.studentsCollection.each(function(model) {
                    this.$('#studentUserSelect').append(this.optionStudentUserTemplate(model.toJSON()));
                }, this);
        }, this)
        });
    },

    render: function() {
        this.$el.html(this.template);
        this._fillStudentUserList();
        this._fillTeacherUserList();
        this._attachEvents();
        return this;
    }

});