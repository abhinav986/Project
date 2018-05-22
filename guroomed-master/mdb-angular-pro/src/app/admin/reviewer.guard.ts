import { Injectable } from '@angular/core';
import { CanActivate } from '@angular/router';
import { Observable } from 'rxjs/Observable';
import { AuthenticationService } from '../services/authentication.service';
import { ToastService } from '../typescripts/pro';

@Injectable()
export class ReviewerGuard implements CanActivate {

  constructor(private autheService: AuthenticationService, private toastrService: ToastService) { }

  canActivate(): Observable<boolean> | Promise<boolean> | boolean {
    if (this.autheService.loggedIn()) {
      if (this.autheService.getUserType() == 'reviewer') {
        return true;
      } else {
        let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
        this.toastrService.error('', 'Unauthorized access!', options);
        return false;
      }
    }
  }
}
