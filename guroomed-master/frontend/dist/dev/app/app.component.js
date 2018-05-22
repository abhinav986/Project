"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var env_config_1 = require("./shared/config/env.config");
var angular2_social_login_1 = require("angular2-social-login");
require("./operators");
var AppComponent = (function () {
    function AppComponent(_auth) {
        this._auth = _auth;
        console.log('Environment config', env_config_1.Config);
    }
    AppComponent.prototype.signIn = function (provider) {
        var _this = this;
        this.sub = this._auth.login(provider).subscribe(function (data) {
            console.log(data);
            _this.user = data;
        });
    };
    AppComponent.prototype.logout = function () {
        var _this = this;
        this._auth.logout().subscribe(function (data) { console.log(data); _this.user = null; });
    };
    AppComponent.prototype.ngOnDestroy = function () {
        this.sub.unsubscribe();
    };
    AppComponent = __decorate([
        core_1.Component({
            moduleId: module.id,
            selector: 'sd-app',
            templateUrl: 'app.component.html',
            styleUrls: ['app.component.css'],
        }),
        __metadata("design:paramtypes", [angular2_social_login_1.AuthService])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9hcHAuY29tcG9uZW50LnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7O0FBQUEsc0NBQXFEO0FBQ3JELHlEQUFvRDtBQUNwRCwrREFBb0Q7QUFDcEQsdUJBQXFCO0FBV3JCO0lBR0Usc0JBQW1CLEtBQWtCO1FBQWxCLFVBQUssR0FBTCxLQUFLLENBQWE7UUFDbkMsT0FBTyxDQUFDLEdBQUcsQ0FBQyxvQkFBb0IsRUFBRSxtQkFBTSxDQUFDLENBQUM7SUFDNUMsQ0FBQztJQUNELDZCQUFNLEdBQU4sVUFBTyxRQUFZO1FBQW5CLGlCQUtDO1FBSkMsSUFBSSxDQUFDLEdBQUcsR0FBRyxJQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQyxRQUFRLENBQUMsQ0FBQyxTQUFTLENBQzdDLFVBQUMsSUFBSTtZQUNILE9BQU8sQ0FBQyxHQUFHLENBQUMsSUFBSSxDQUFDLENBQUM7WUFBQSxLQUFJLENBQUMsSUFBSSxHQUFDLElBQUksQ0FBQztRQUFBLENBQUMsQ0FDckMsQ0FBQTtJQUNILENBQUM7SUFFRCw2QkFBTSxHQUFOO1FBQUEsaUJBSUM7UUFIQyxJQUFJLENBQUMsS0FBSyxDQUFDLE1BQU0sRUFBRSxDQUFDLFNBQVMsQ0FDM0IsVUFBQyxJQUFJLElBQUksT0FBTyxDQUFDLEdBQUcsQ0FBQyxJQUFJLENBQUMsQ0FBQyxDQUFBLEtBQUksQ0FBQyxJQUFJLEdBQUMsSUFBSSxDQUFDLENBQUEsQ0FBQyxDQUM1QyxDQUFBO0lBQ0gsQ0FBQztJQUVELGtDQUFXLEdBQVg7UUFDRSxJQUFJLENBQUMsR0FBRyxDQUFDLFdBQVcsRUFBRSxDQUFDO0lBQ3pCLENBQUM7SUFyQlUsWUFBWTtRQU54QixnQkFBUyxDQUFDO1lBQ1QsUUFBUSxFQUFFLE1BQU0sQ0FBQyxFQUFFO1lBQ25CLFFBQVEsRUFBRSxRQUFRO1lBQ2xCLFdBQVcsRUFBRSxvQkFBb0I7WUFDakMsU0FBUyxFQUFFLENBQUMsbUJBQW1CLENBQUM7U0FDakMsQ0FBQzt5Q0FJMEIsbUNBQVc7T0FIMUIsWUFBWSxDQXNCeEI7SUFBRCxtQkFBQztDQXRCRCxBQXNCQyxJQUFBO0FBdEJZLG9DQUFZIiwiZmlsZSI6ImFwcC9hcHAuY29tcG9uZW50LmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgQ29tcG9uZW50LCBPbkRlc3Ryb3kgfSBmcm9tICdAYW5ndWxhci9jb3JlJztcclxuaW1wb3J0IHsgQ29uZmlnIH0gZnJvbSAnLi9zaGFyZWQvY29uZmlnL2Vudi5jb25maWcnO1xyXG5pbXBvcnQgeyBBdXRoU2VydmljZSB9IGZyb20gXCJhbmd1bGFyMi1zb2NpYWwtbG9naW5cIjtcclxuaW1wb3J0ICcuL29wZXJhdG9ycyc7XHJcblxyXG4vKipcclxuICogVGhpcyBjbGFzcyByZXByZXNlbnRzIHRoZSBtYWluIGFwcGxpY2F0aW9uIGNvbXBvbmVudC5cclxuICovXHJcbkBDb21wb25lbnQoe1xyXG4gIG1vZHVsZUlkOiBtb2R1bGUuaWQsXHJcbiAgc2VsZWN0b3I6ICdzZC1hcHAnLFxyXG4gIHRlbXBsYXRlVXJsOiAnYXBwLmNvbXBvbmVudC5odG1sJyxcclxuICBzdHlsZVVybHM6IFsnYXBwLmNvbXBvbmVudC5jc3MnXSxcclxufSlcclxuZXhwb3J0IGNsYXNzIEFwcENvbXBvbmVudCBpbXBsZW1lbnRzIE9uRGVzdHJveSB7XHJcbiAgcHVibGljIHVzZXI6YW55O1xyXG4gIHN1YjogYW55O1xyXG4gIGNvbnN0cnVjdG9yKHB1YmxpYyBfYXV0aDogQXV0aFNlcnZpY2UpIHtcclxuICAgIGNvbnNvbGUubG9nKCdFbnZpcm9ubWVudCBjb25maWcnLCBDb25maWcpO1xyXG4gIH1cclxuICBzaWduSW4ocHJvdmlkZXI6YW55KXtcclxuICAgIHRoaXMuc3ViID0gdGhpcy5fYXV0aC5sb2dpbihwcm92aWRlcikuc3Vic2NyaWJlKFxyXG4gICAgICAoZGF0YSkgPT4ge1xyXG4gICAgICAgIGNvbnNvbGUubG9nKGRhdGEpO3RoaXMudXNlcj1kYXRhO31cclxuICAgIClcclxuICB9XHJcblxyXG4gIGxvZ291dCgpe1xyXG4gICAgdGhpcy5fYXV0aC5sb2dvdXQoKS5zdWJzY3JpYmUoXHJcbiAgICAgIChkYXRhKT0+e2NvbnNvbGUubG9nKGRhdGEpO3RoaXMudXNlcj1udWxsO31cclxuICAgIClcclxuICB9XHJcblxyXG4gIG5nT25EZXN0cm95KCl7XHJcbiAgICB0aGlzLnN1Yi51bnN1YnNjcmliZSgpO1xyXG4gIH1cclxufVxyXG4iXX0=
