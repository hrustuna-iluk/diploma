var TeacherJournalView = BaseView.extend({

    template: _.template($("#tabTemplate").html()),

    currentTab: null,

    initialize: function(options) {
        this.group = options.group;
        this.studentsCollection = options.studentsCollection;
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
            model: this.group
        });
        this._tabChanged('wrapTab', wrapTabView);
    },

    _publicOrdersTab: function(){
        var publicOrdersTabView = new PublicOrdersTabView({
            model: this.group
        });
        this._tabChanged('publicOrdersTab', publicOrdersTabView);
    },

    _dataTab: function(){
        this._tabChanged();
    },

    _allInformationTab: function(){
        this._tabChanged();
    },

    _publicPlanTab: function(){
        this._tabChanged();
    },

    _attendanceTab: function(){
        this._tabChanged();
    },

    _educationalEventsTab: function(){
        this._tabChanged();
    },

    _individualWorkTab: function(){
        this._tabChanged();
    },

    _reportTab: function(){
        this._tabChanged();
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