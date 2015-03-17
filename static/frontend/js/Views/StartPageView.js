var StartPageView = BaseView.extend ({

    tagName: "div",

    template: _.template($("#startPageTemplate").html()),

    selectors: {
        createDepartment: "#addDepartment",
        changeDepartment: "#changeDepartment",
        departmentTitle: "#departmentName"
    },

    constants: {
        ENTER_KEY_CODE: 13
    },

    initialize: function(options) {
        this.collection = options.collection;
        this.collection.on("add", $.proxy(this._renderDepartment, this));
        this.publisher.on('change department', $.proxy(this._onDepartmentChange, this));
        this.collection.reset().fetch();
    },

    _attachEvents: function() {
        this.$(this.selectors.createDepartment).on('click', $.proxy(this._addDepartment, this));
        this.$(this.selectors.changeDepartment).on('click', $.proxy(this._changeDepartment, this));
        this.$(this.selectors.departmentTitle).on('keypress', $.proxy(this._onEnter, this))

    },

    _onDepartmentChange: function(model) {
        $(this.selectors.departmentTitle).val(model.getTitle());
        this.$(this.selectors.changeDepartment).data('model', model);
        this.$(this.selectors.createDepartment).addClass('no-display');
        this.$(this.selectors.changeDepartment).removeClass('no-display');
    },

    _onEnter: function(e) {
        if(e.keyCode === this.constants.ENTER_KEY_CODE) {
            this._addDepartment();
        }
    },

    _addDepartment: function() {
        var departmentModel = new DepartmentModel();
        var departmentTitle = this.$(this.selectors.departmentTitle).val();
        this.$(this.selectors.departmentTitle).val("");
        departmentModel.setTitle(departmentTitle);
        departmentModel.save({wait: true}, {success: $.proxy(function() {
                    this.collection.add(departmentModel);
                }, this)});
        return false;
    },

    _changeDepartment: function() {
        var departmentModel = this.$(this.selectors.changeDepartment).data('model');
        var departmentTitle = this.$(this.selectors.departmentTitle).val();
        this.$(this.selectors.departmentTitle).val("");
        departmentModel.setTitle(departmentTitle);
        this.$(this.selectors.changeDepartment).addClass('no-display');
        this.$(this.selectors.createDepartment).removeClass('no-display');
    },

    _renderDepartment: function(model) {
        this.$("#departments").append(
            new DepartmentView({
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