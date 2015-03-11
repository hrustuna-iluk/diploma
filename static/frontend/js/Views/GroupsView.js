var GroupsView = BaseView.extend({

    template: _.template($("#groupsTemplate").html()),

    selectors: {
        createGroup: "#addGroup",
        changeGroup: "#changeGroup",
        groupNumber: "#groupNumber",
        groupYear: "#groupYear",
        groupTuition: "#groupTuition"
    },

    initialize: function(options) {
        this.collection = options.collection;
        this.collection.on("add", $.proxy(this._renderGroup, this));
        this.publisher.on('change group', $.proxy(this._onGroupChange, this));
    },

    _attachEvents: function() {
        this.$(this.selectors.createGroup).on('click', $.proxy(this._addGroup, this));
        this.$(this.selectors.changeGroup).on('click', $.proxy(this._changeGroup, this));
    },

    _onGroupChange: function(model) {
        $(this.selectors.groupNumber).val(model.getNumber());
        $(this.selectors.groupTuition).val(model.getTuition());
        $(this.selectors.groupYear).val(model.getYearStudy());
        this.$(this.selectors.changeGroup).data('model', model);
        this.$(this.selectors.createGroup).addClass('no-display');
        this.$(this.selectors.changeGroup).removeClass('no-display');
    },

    _groupData: function(groupModel) {
        var groupNumber = this.$(this.selectors.groupNumber).val(),
            groupTuition = this.$(this.selectors.groupTuition).val(),
            groupYear = this.$(this.selectors.groupYear).val();
        this.$(this.selectors.groupNumber).val("");
        this.$(this.selectors.groupTuition).val("");
        this.$(this.selectors.groupYear).val("");
        groupModel.setNumber(groupNumber);
        groupModel.setTuition(groupTuition);
        groupModel.setYearStudy(groupYear);

    },

    _addGroup: function() {
        var groupModel = new GroupModel();
        this._groupData(groupModel);
        this.collection.add(groupModel);
    },

    _changeGroup: function() {
        var groupModel = this.$(this.selectors.changeGroup).data('model');
        this._groupData(groupModel);
        this.$(this.selectors.changeGroup).addClass('no-display');
        this.$(this.selectors.createGroup).removeClass('no-display');
    },

    _renderGroup: function(model) {
        this.$("#groups").append(
            new GroupView({
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