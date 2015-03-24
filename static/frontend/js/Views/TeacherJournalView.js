var TeacherJournalView = BaseView.extend({

    template: _.template($("#tabTemplate").html()),

    currentTab: null,

    currentForm: null,

    initialize: function(options) {
        this.group = options.group;
        this.studentsCollection = options.studentsCollection;
        this.publicPlanCollection = options.publicPlanCollection;
    },

    _attachEvents: function() {
        this.$('.wrapTab').on('click', $.proxy(this._wrapTab, this));
        this.$('.publicOrdersTab').on('click', $.proxy(this._publicOrdersTab, this));
        this.$('.dataTab').on('click', $.proxy(this._dataTab, this));
        this.$('.allInformationTab').on('click', $.proxy(this._allInformationTab, this));
        this.$('.publicPlanTab').on('click', $.proxy(this._publicPlanTab, this));
        this.$('.attendanceTab').on('click', $.proxy(this._attendanceTab, this));
        this.$('.educationalEventsTab').on('click', $.proxy(this._educationalEventsTab, this));
        this.$('.individualWorkTab').on('click', $.proxy(this._individualWorkTab, this));
        this.$('.reportTab').on('click', $.proxy(this._reportTab, this));
    },

    _wrapTab: function(){
        var wrapTabView = new WrapTabView({
            group: this.group
        });
        this._tabChanged('wrapTab', wrapTabView);
        this._formChanged();
    },

    _publicOrdersTab: function(){
        var publicOrdersTabView = new PublicOrdersTabView({
            group: this.group
        });
        this._tabChanged('publicOrdersTab', publicOrdersTabView);
        this._formChanged();
    },

    _dataTab: function(){
        var dataTabView = new DataTabView({
            group: this.group,
            collection: this.studentsCollection
        });
        this._tabChanged('dataTab',dataTabView);
        this._formChanged();
    },

    _allInformationTab: function(){
        var allInformationTabView = new AllInformationTabView({
            group: this.group,
            collection: this.studentsCollection
        });
        this._tabChanged('allInformationTab', allInformationTabView);
        this._formChanged();
    },

    _publicPlanTab: function(){
        var publicPlanTabView = new PublicPlanTabView({
            group: this.group,
            publicPlanCollection: this.publicPlanCollection
        });
        var publicPlanTabForm = new PublicPlanTabFormView({
            publicPlanCollection: this.publicPlanCollection
        });
        this._tabChanged('publicPlanTab', publicPlanTabView);
        this._formChanged(publicPlanTabForm);
    },

    _attendanceTab: function(){
        this._tabChanged();
    },

    _educationalEventsTab: function(){
        var publicEventsTabView = new PublicEventsTabView({
            group: this.group,
            publicPlanCollection: this.publicPlanCollection
        });
        var publicEventsTabForm = new PublicEventsTabFormView({
            publicPlanCollection: this.publicPlanCollection
        });
        this._tabChanged('educationalEventsTab', publicEventsTabView);
        this._formChanged(publicEventsTabForm);
    },

    _individualWorkTab: function(){
        this._tabChanged();
    },

    _reportTab: function(){
        this._tabChanged();
    },

    _formChanged: function(form) {
        if (this.currentForm) {
            this.currentForm.remove();
        }
        if(form) {
            $('#formForTab .forms').html(form.render().el);
            this.currentForm = form;
        }
    },

    _tabChanged: function(div_id,tab) {
        if (this.currentTab) {
            this.currentTab.remove();
        }
        $('#'+ div_id).html( tab.render().el );
        this.currentTab = tab;
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        this._wrapTab();
        return this;
    }

});