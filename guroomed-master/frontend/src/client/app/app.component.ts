import { Component, OnDestroy } from '@angular/core';
import { Config } from './shared/config/env.config';
import { AuthService } from "angular2-social-login";
import './operators';

/**
 * This class represents the main application component.
 */
@Component({
  moduleId: module.id,
  selector: 'sd-app',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.css'],
})
export class AppComponent implements OnDestroy {
  public user:any;
  sub: any;
  constructor(public _auth: AuthService) {
    console.log('Environment config', Config);
  }
  signIn(provider:any){
    this.sub = this._auth.login(provider).subscribe(
      (data) => {
        console.log(data);this.user=data;}
    )
  }

  logout(){
    this._auth.logout().subscribe(
      (data)=>{console.log(data);this.user=null;}
    )
  }

  ngOnDestroy(){
    this.sub.unsubscribe();
  }
}
