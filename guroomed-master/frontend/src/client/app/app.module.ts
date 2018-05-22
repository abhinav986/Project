import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { APP_BASE_HREF } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { AboutModule } from './about/about.module';
import { HomeModule } from './home/home.module';
import { SharedModule } from './shared/shared.module';
import { Angular2SocialLoginModule } from "angular2-social-login";
import { LoginModule } from './login/login.module';

let Socialproviders = {
    "google": {
      "clientId": "659654452019-7cmffctlmudlg1ehl4idhbv3410pou2r.apps.googleusercontent.com"
    },
    "facebook": {
      "clientId": "111928296072462",
      "apiVersion": "v2.4"
    }
  };



@NgModule({
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    AboutModule,
    HomeModule,
    LoginModule,
    Angular2SocialLoginModule
  ],
  declarations: [AppComponent],
  providers: [{
    provide: APP_BASE_HREF,
    useValue: '<%= APP_BASE %>'
  }],
  bootstrap: [AppComponent]

})
export class AppModule { }
Angular2SocialLoginModule.loadProvidersScripts(Socialproviders);

