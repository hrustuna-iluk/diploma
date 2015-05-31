var GroupsView = BaseView.extend({

    template: _.template($("#groupsTemplate").html()),

    optionCuratorTemplate: _.template('<option value="<%=id%>"><%=lastName%> <%=firstName%> <%=middleName%></option>'),

    selectors: {
        createGroup: "#addGroup",
        changeGroup: "#changeGroup",
        groupNumber: "#groupNumber",
        groupYear: "#groupYear",
        groupTuition: "#groupTuition",
        groupCurator: "#groupCurator",
        addCurator: "#addCurator"
    },

    initialize: function(options) {
        this.collection = options.collection;
        this.department = options.department;
        this.teachersCollection = options.teachersCollection;
        this.collection.on("add", $.proxy(this._renderGroup, this));
        //this.teachersCollection.on("add", $.proxy(this._fillCuratorList, this));
        this.publisher.on('change:group', $.proxy(this._onGroupChange, this));
        this.collection.reset().fetch({data: {
            department: this.department.get('id')
        }, processData: true});
    },

    _attachEvents: function() {
        this.$(this.selectors.createGroup).on('click', $.proxy(this._addGroup, this));
        this.$(this.selectors.changeGroup).on('click', $.proxy(this._changeGroup, this));
        this.$(this.selectors.addCurator).on('click', $.proxy(this._addCurator, this));
        this.teachersCollection.on('add remove reset', $.proxy(this._fillCuratorList, this));
    },

    _addCurator: function(){
        this.addTeacherModal = new AddTeacherModalView({
            department: this.department,
            collection: this.teachersCollection
        }).render().$el;
    },

    _onGroupChange: function(model) {
        $(this.selectors.groupNumber).val(model.getNumber());
        $(this.selectors.groupTuition).val(model.getTuition());
        $(this.selectors.groupYear).val(model.getYearStudy());
        $(this.selectors.groupCurator).val(_.isObject(model.getCurator()) ? model.getCurator().id : model.getCurator());
        this.$(this.selectors.changeGroup).data('model', model);
        this.$(this.selectors.createGroup).addClass('no-display');
        this.$(this.selectors.changeGroup).removeClass('no-display');
    },

    _groupData: function(groupModel) {
        var groupNumber = this.$(this.selectors.groupNumber).val(),
            groupTuition = this.$(this.selectors.groupTuition).val(),
            groupYear = this.$(this.selectors.groupYear).val();
        groupModel.setNumber(groupNumber);
        groupModel.setTuition(groupTuition);
        groupModel.setYearStudy(groupYear);
        groupModel.set('department', this.department.get('id'));
        groupModel.set('curator', +this.$(this.selectors.groupCurator).val() || null);
        this.$(this.selectors.groupNumber).val("");
        this.$(this.selectors.groupTuition).val("");
        this.$(this.selectors.groupYear).val("");
        this.$(this.selectors.groupCurator).find('option:first').attr('selected', true);

    },

    _addGroup: function() {
        var groupModel = new GroupModel();
        this._groupData(groupModel);
        groupModel.save({wait: true}, {success: $.proxy(function() {
                    this.collection.add(groupModel);
                }, this)});
    },

    _changeGroup: function() {
        var groupModel = this.$(this.selectors.changeGroup).data('model');
        this._groupData(groupModel);
        groupModel.save();
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


    _fillCuratorList: function(model) {
        this.$('#groupCurator').empty();
        this.teachersCollection.each(function(model) {
            this.$('#groupCurator').append(this.optionCuratorTemplate(model.toJSON()));
        }, this);
    },

    render: function() {
        this.$el.html(this.template(this.department.toJSON()));
        this._attachEvents();
        this._fillCuratorList();
        return this;
    }
});