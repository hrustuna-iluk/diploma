var Route = Backbone.Router.extend({

    routes: {
        "": "startPage",
        'teachers/:departmentId': 'teachers',
        'groups/:departmentId' : 'groups',
        'students/:groupId' : 'students',
        'reduction/:groupId': 'reduction',
        'scheduler/:groupId': 'scheduler',
        'journal/:groupId': 'journal'
    },

    currentView: null,

    initialize: function() {
        this.departmentsCollection = new DepartmentsCollection();
        this.teachersCollection = new TeachersCollection();
        this.groupsCollection = new GroupsCollection();
        this.studentsCollection = new StudentsCollection();
        this.passesCollection = new PassesCollection();
        this.classesCollection = new ClassesCollection();
        this.languagesCollection = new LanguagesCollection();
        this.benefitsCollection = new BenefitsCollection();
        this.publicOrdersCollection = new PublicOrdersCollection();
        this.attendanceCollection = new AttendanceCollection();
        this._initializeEvents();

    },

    _initializeEvents: function() {
        this.on('route:startPage', this.startPage);
        this.on('route:teachers:', this.teachers);
        this.on('route:groups:', this.teachers);
        this.on('route:students:', this.students);
        this.on('route:reduction:', this.reduction);
        this.on('route:scheduler:', this.scheduler);
        this.on('route:journal:', this.journal);

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
            collection: this.studentsCollection,
            benefitsCollection: this.benefitsCollection,
            publicOrdersCollection: this.publicOrdersCollection,
            languagesCollection: this.languagesCollection
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
        var reduction = this.attendanceCollection.find({group:groupId});
        if(!reduction) {
            reduction = new AttendanceModel({
                group: group
            })
        }
        var reductionView = new ReductionView({
            model: reduction,
            group: group,
            collection: this.passesCollection
        });
        this.routeChanged(reductionView);
    },

    scheduler: function(groupId) {
        //this.classesCollection.fetch();
        var group = this.groupsCollection.findWhere({cid: groupId});
        var schedulerView = new ScheduleView({
            group: group,
            collection: this.classesCollection,
            teacherCollection: this.teacherCollection
        });
        this.routeChanged(schedulerView);
    },

    journal: function(groupId) {
        var group = this.groupsCollection.findWhere({cid: groupId});
        var tabView = new TabView({
            group: group,
            collection: this.studentsCollection
        });
        this.routeChanged(tabView);
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