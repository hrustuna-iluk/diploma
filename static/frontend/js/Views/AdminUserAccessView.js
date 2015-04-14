var AdminUserAccessView = BaseView.extend({

    template: _.template($("#adminUserAccessTemplate").html()),

    optionStudentUserTemplate: _.template($("#optionStudentUserTemplate").html()),

    optionTeacherUserTemplate: _.template($("#optionTeacherUserTemplate").html()),

    initialize: function(options) {
        this.studentsCollection = options.studentsCollection;
        this.teachersCollection = options.teachersCollection;
        this.collection = options.usersCollection;
        this.collection.on("add", $.proxy(this._renderUser, this));
    },

    _attachEvents: function() {
        this.$('#addTeacherUser').on('click', $.proxy(this._addTeacherUser, this));
        this.$('#addStudentUser').on('click', $.proxy(this._addStudentUser, this));
    },

    _addTeacherUser: function() {
        var value = this.$('[name=teacherUserSelect]').val();
        var userModel = new UserModel({
            username: this.$('#teacherUserLogin').val(),
            password: this.$('#teacherUserPassword').val()
        });
        var teacherId = this.$('#teacherUserSelect').find('[value="' + value + '"]').data('id');

        var teacher = this.teachersCollection.findWhere({ id: teacherId });
        teacher.set({
            user: userModel
        });
        this.teacher.save({
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
        var userModel = new UserModel({
            username: this.$('#studentUserLogin').val(),
            password: this.$('#studentUserPassword').val()
        });
        var studentId = this.$('#studentUserSelect').find('[value="' + value + '"]').data('id');
        var student = this.studentsCollection.findWhere({ id: studentId });
        student.set({
            user: userModel
        });
        this.student.save({
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