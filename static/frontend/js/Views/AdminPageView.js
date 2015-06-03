var AdminPageView = BaseView.extend({

    template: _.template($("#adminPage").html()),

    currentView: null,

    initialize: function(options) {
        this.faculty = options.faculty;
        this.teachersCollection = options.teachersCollection;
        this.studentsCollection = options.studentsCollection;
        this.groupsCollection = options.groupsCollection;
        this.departmentsCollection = options.departmentsCollection;
    },

    _attachEvents: function(){
        this.$('.adminInformationAboutFaculty').on('click', $.proxy(this._addFacultyInformation, this));
        this.$('.adminReduction').on('click', $.proxy(this._adminReduction, this));
        this.$('.adminUserAccess').on('click', $.proxy(this._addUser, this));
        this.$('.deletePasses').on('click', $.proxy(this._deletePasses, this));
    },

    _addFacultyInformation: function() {
        var informationView = new AdminInformationAboutFacultyView({
            faculty: this.faculty
        });
        this._viewChanged(informationView);
    },

    _adminReduction: function() {
        var reductionView = new AdminReductionView({
            groupsCollection: this.groupsCollection,
            departmentsCollection: this.departmentsCollection,
            faculty: this.faculty
        });
        this._viewChanged(reductionView);
    },

    _addUser: function() {
        var userView = new AdminUserAccessView({
            teachersCollection: this.teachersCollection,
            studentsCollection: this.studentsCollection,
            groupsCollection: this.groupsCollection
        });
        this._viewChanged(userView);
    },

    _viewChanged: function(view) {
        if (this.currentView) {
            this.currentView.remove();
        }
        $('#adminContent').html( view.render().el );
        this.currentView = view;
    },

    _deletePasses: function() {
        if (confirm('Ви справді хочете видалити пропуски?')) {
            $.post('/app/deletePasses/', $.proxy(function (resp) {
            alert(resp.message);
        }, this));
        }
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }

});