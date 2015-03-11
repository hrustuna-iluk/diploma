var Route = Backbone.Router.extend({

    routes: {
        "": "startPage",
        'teachers/:departmentId': 'teachers',
        'groups/:departmentId' : 'groups',
        'students/:groupId' : 'students',
        'reduction/:groupId': 'reduction',
        'scheduler/:groupId': 'scheduler'//,
        //'teacherJournal/:groupId': 'journal'
    },

    currentView: null,

    initialize: function() {
        this.departmentsCollection = new DepartmentsCollection();
        this.teachersCollection = new TeachersCollection();
        this.groupsCollection = new GroupsCollection();
        this.studentsCollection = new StudentsCollection();
        this.passesCollection = new PassesCollection();
        this.classesCollection = new ClassesCollection();
        this._initializeEvents();

    },

    _initializeEvents: function() {
        this.on('route:startPage', this.startPage);
        this.on('route:teachers:', this.teachers);
        this.on('route:groups:', this.teachers);
        this.on('route:students:', this.students);
        this.on('route:reduction:', this.reduction);
        this.on('route:scheduler:', this.scheduler);

    },

    startPage: function() {
        var startPageView = new StartPageView({
            collection: this.departmentsCollection
        });
        this.routeChanged(startPageView);
    },

    teachers: function(departmentId) {
        var department = this.departmentsCollection.findWhere({cid: departmentId});
        var teachersView = new TeachersView({
            department: department,
            collection: this.teachersCollection
        });
        this.routeChanged(teachersView);
    },

    students: function(groupId) {
        var group = this.groupsCollection.findWhere({cid: groupId});
        var studentsView = new StudentsView({
            group: group,
            collection: this.studentsCollection
        });
        this.routeChanged(studentsView);
    },

    groups: function(departmentId) {
        var department = this.departmentsCollection.findWhere({cid: departmentId});
        var groupsView = new GroupsView({
            department: department,
            collection: this.groupsCollection
        });
        this.routeChanged(groupsView);
    },

    reduction: function(groupId) {
        var group = this.groupsCollection.findWhere({cid: groupId});
        var reductionView = new ReductionView({
            group: group,
            collection: this.passesCollection
        });
        this.routeChanged(reductionView);
    },

    scheduler: function(groupId) {
        var group = this.groupsCollection.findWhere({cid: groupId});
        var schedulerView = new SchedulerView({
            group: group,
            collection: this.classesCollection
        });
        this.routeChanged(schedulerView);
    },

    routeChanged: function(view) {
        if (this.currentView) {
            this.currentView.remove();
        }
        $('body').html( view.render().el );
        this.currentView = view;
    }
});

var route = new Route;
Backbone.history.start();