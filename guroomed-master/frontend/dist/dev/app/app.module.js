"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var platform_browser_1 = require("@angular/platform-browser");
var common_1 = require("@angular/common");
var http_1 = require("@angular/common/http");
var app_component_1 = require("./app.component");
var app_routing_module_1 = require("./app-routing.module");
var about_module_1 = require("./about/about.module");
var home_module_1 = require("./home/home.module");
var angular2_social_login_1 = require("angular2-social-login");
var login_module_1 = require("./login/login.module");
var Socialproviders = {
    "google": {
        "clientId": "659654452019-7cmffctlmudlg1ehl4idhbv3410pou2r.apps.googleusercontent.com"
    },
    "facebook": {
        "clientId": "111928296072462",
        "apiVersion": "v2.4"
    }
};
var AppModule = (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        core_1.NgModule({
            imports: [
                platform_browser_1.BrowserModule,
                http_1.HttpClientModule,
                app_routing_module_1.AppRoutingModule,
                about_module_1.AboutModule,
                home_module_1.HomeModule,
                login_module_1.LoginModule,
                angular2_social_login_1.Angular2SocialLoginModule
            ],
            declarations: [app_component_1.AppComponent],
            providers: [{
                    provide: common_1.APP_BASE_HREF,
                    useValue: '/'
                }],
            bootstrap: [app_component_1.AppComponent]
        })
    ], AppModule);
    return AppModule;
}());
exports.AppModule = AppModule;
angular2_social_login_1.Angular2SocialLoginModule.loadProvidersScripts(Socialproviders);

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9hcHAubW9kdWxlLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUEsc0NBQXlDO0FBQ3pDLDhEQUEwRDtBQUMxRCwwQ0FBZ0Q7QUFDaEQsNkNBQXdEO0FBQ3hELGlEQUErQztBQUMvQywyREFBd0Q7QUFDeEQscURBQW1EO0FBQ25ELGtEQUFnRDtBQUVoRCwrREFBa0U7QUFDbEUscURBQW1EO0FBRW5ELElBQUksZUFBZSxHQUFHO0lBQ2xCLFFBQVEsRUFBRTtRQUNSLFVBQVUsRUFBRSwwRUFBMEU7S0FDdkY7SUFDRCxVQUFVLEVBQUU7UUFDVixVQUFVLEVBQUUsaUJBQWlCO1FBQzdCLFlBQVksRUFBRSxNQUFNO0tBQ3JCO0NBQ0YsQ0FBQztBQXNCSjtJQUFBO0lBQXlCLENBQUM7SUFBYixTQUFTO1FBbEJyQixlQUFRLENBQUM7WUFDUixPQUFPLEVBQUU7Z0JBQ1AsZ0NBQWE7Z0JBQ2IsdUJBQWdCO2dCQUNoQixxQ0FBZ0I7Z0JBQ2hCLDBCQUFXO2dCQUNYLHdCQUFVO2dCQUNWLDBCQUFXO2dCQUNYLGlEQUF5QjthQUMxQjtZQUNELFlBQVksRUFBRSxDQUFDLDRCQUFZLENBQUM7WUFDNUIsU0FBUyxFQUFFLENBQUM7b0JBQ1YsT0FBTyxFQUFFLHNCQUFhO29CQUN0QixRQUFRLEVBQUUsaUJBQWlCO2lCQUM1QixDQUFDO1lBQ0YsU0FBUyxFQUFFLENBQUMsNEJBQVksQ0FBQztTQUUxQixDQUFDO09BQ1csU0FBUyxDQUFJO0lBQUQsZ0JBQUM7Q0FBMUIsQUFBMEIsSUFBQTtBQUFiLDhCQUFTO0FBQ3RCLGlEQUF5QixDQUFDLG9CQUFvQixDQUFDLGVBQWUsQ0FBQyxDQUFDIiwiZmlsZSI6ImFwcC9hcHAubW9kdWxlLmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgTmdNb2R1bGUgfSBmcm9tICdAYW5ndWxhci9jb3JlJztcclxuaW1wb3J0IHsgQnJvd3Nlck1vZHVsZSB9IGZyb20gJ0Bhbmd1bGFyL3BsYXRmb3JtLWJyb3dzZXInO1xyXG5pbXBvcnQgeyBBUFBfQkFTRV9IUkVGIH0gZnJvbSAnQGFuZ3VsYXIvY29tbW9uJztcclxuaW1wb3J0IHsgSHR0cENsaWVudE1vZHVsZSB9IGZyb20gJ0Bhbmd1bGFyL2NvbW1vbi9odHRwJztcclxuaW1wb3J0IHsgQXBwQ29tcG9uZW50IH0gZnJvbSAnLi9hcHAuY29tcG9uZW50JztcclxuaW1wb3J0IHsgQXBwUm91dGluZ01vZHVsZSB9IGZyb20gJy4vYXBwLXJvdXRpbmcubW9kdWxlJztcclxuaW1wb3J0IHsgQWJvdXRNb2R1bGUgfSBmcm9tICcuL2Fib3V0L2Fib3V0Lm1vZHVsZSc7XHJcbmltcG9ydCB7IEhvbWVNb2R1bGUgfSBmcm9tICcuL2hvbWUvaG9tZS5tb2R1bGUnO1xyXG5pbXBvcnQgeyBTaGFyZWRNb2R1bGUgfSBmcm9tICcuL3NoYXJlZC9zaGFyZWQubW9kdWxlJztcclxuaW1wb3J0IHsgQW5ndWxhcjJTb2NpYWxMb2dpbk1vZHVsZSB9IGZyb20gXCJhbmd1bGFyMi1zb2NpYWwtbG9naW5cIjtcclxuaW1wb3J0IHsgTG9naW5Nb2R1bGUgfSBmcm9tICcuL2xvZ2luL2xvZ2luLm1vZHVsZSc7XHJcblxyXG5sZXQgU29jaWFscHJvdmlkZXJzID0ge1xyXG4gICAgXCJnb29nbGVcIjoge1xyXG4gICAgICBcImNsaWVudElkXCI6IFwiNjU5NjU0NDUyMDE5LTdjbWZmY3RsbXVkbGcxZWhsNGlkaGJ2MzQxMHBvdTJyLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tXCJcclxuICAgIH0sXHJcbiAgICBcImZhY2Vib29rXCI6IHtcclxuICAgICAgXCJjbGllbnRJZFwiOiBcIjExMTkyODI5NjA3MjQ2MlwiLFxyXG4gICAgICBcImFwaVZlcnNpb25cIjogXCJ2Mi40XCJcclxuICAgIH1cclxuICB9O1xyXG5cclxuXHJcblxyXG5ATmdNb2R1bGUoe1xyXG4gIGltcG9ydHM6IFtcclxuICAgIEJyb3dzZXJNb2R1bGUsXHJcbiAgICBIdHRwQ2xpZW50TW9kdWxlLFxyXG4gICAgQXBwUm91dGluZ01vZHVsZSxcclxuICAgIEFib3V0TW9kdWxlLFxyXG4gICAgSG9tZU1vZHVsZSxcclxuICAgIExvZ2luTW9kdWxlLFxyXG4gICAgQW5ndWxhcjJTb2NpYWxMb2dpbk1vZHVsZVxyXG4gIF0sXHJcbiAgZGVjbGFyYXRpb25zOiBbQXBwQ29tcG9uZW50XSxcclxuICBwcm92aWRlcnM6IFt7XHJcbiAgICBwcm92aWRlOiBBUFBfQkFTRV9IUkVGLFxyXG4gICAgdXNlVmFsdWU6ICc8JT0gQVBQX0JBU0UgJT4nXHJcbiAgfV0sXHJcbiAgYm9vdHN0cmFwOiBbQXBwQ29tcG9uZW50XVxyXG5cclxufSlcclxuZXhwb3J0IGNsYXNzIEFwcE1vZHVsZSB7IH1cclxuQW5ndWxhcjJTb2NpYWxMb2dpbk1vZHVsZS5sb2FkUHJvdmlkZXJzU2NyaXB0cyhTb2NpYWxwcm92aWRlcnMpO1xyXG5cclxuIl19
