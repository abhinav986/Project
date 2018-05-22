"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var common_1 = require("@angular/common");
var essearch_component_1 = require("./essearch/essearch.component");
var ElasticsearchModule = (function () {
    function ElasticsearchModule() {
    }
    ElasticsearchModule = __decorate([
        core_1.NgModule({
            imports: [
                common_1.CommonModule
            ],
            exports: [essearch_component_1.EssearchComponent],
            declarations: [essearch_component_1.EssearchComponent]
        })
    ], ElasticsearchModule);
    return ElasticsearchModule;
}());
exports.ElasticsearchModule = ElasticsearchModule;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9lbGFzdGljc2VhcmNoL2VsYXN0aWNzZWFyY2gubW9kdWxlLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUEsc0NBQXlDO0FBQ3pDLDBDQUErQztBQUMvQyxvRUFBa0U7QUFTbEU7SUFBQTtJQUFtQyxDQUFDO0lBQXZCLG1CQUFtQjtRQVAvQixlQUFRLENBQUM7WUFDUixPQUFPLEVBQUU7Z0JBQ1AscUJBQVk7YUFDYjtZQUNELE9BQU8sRUFBQyxDQUFDLHNDQUFpQixDQUFDO1lBQzNCLFlBQVksRUFBRSxDQUFDLHNDQUFpQixDQUFDO1NBQ2xDLENBQUM7T0FDVyxtQkFBbUIsQ0FBSTtJQUFELDBCQUFDO0NBQXBDLEFBQW9DLElBQUE7QUFBdkIsa0RBQW1CIiwiZmlsZSI6ImFwcC9lbGFzdGljc2VhcmNoL2VsYXN0aWNzZWFyY2gubW9kdWxlLmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgTmdNb2R1bGUgfSBmcm9tICdAYW5ndWxhci9jb3JlJztcclxuaW1wb3J0IHsgQ29tbW9uTW9kdWxlIH0gZnJvbSAnQGFuZ3VsYXIvY29tbW9uJztcclxuaW1wb3J0IHsgRXNzZWFyY2hDb21wb25lbnQgfSBmcm9tICcuL2Vzc2VhcmNoL2Vzc2VhcmNoLmNvbXBvbmVudCc7XHJcblxyXG5ATmdNb2R1bGUoe1xyXG4gIGltcG9ydHM6IFtcclxuICAgIENvbW1vbk1vZHVsZVxyXG4gIF0sXHJcbiAgZXhwb3J0czpbRXNzZWFyY2hDb21wb25lbnRdLFxyXG4gIGRlY2xhcmF0aW9uczogW0Vzc2VhcmNoQ29tcG9uZW50XVxyXG59KVxyXG5leHBvcnQgY2xhc3MgRWxhc3RpY3NlYXJjaE1vZHVsZSB7IH1cclxuIl19
