import pytest
import context
from twitter_bot.parsecard import ParseCard
CARD = """
<div class="ProfileCard js-actionable-user
    " data-screen-name="matt_klein" data-user-id="18007153" data-feedback-token="" data-impression-id="">
  <a class="ProfileCard-bg js-nav" href="/matt_klein" tabindex="-1" aria-hidden="true" style="
    background-color: #3B94D9;
    ">
  </a>

  <div class="ProfileCard-content">
    <a class="ProfileCard-avatarLink js-nav js-tooltip" href="/matt_klein" tabindex="-1" aria-hidden="true" data-original-title="Matt Klein">
      <img class="ProfileCard-avatarImage js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/411745054/DSC_2431_bigger.jpg" alt="">
    </a>
    
      <div class="ProfileCard-actions">
        <div class="ProfileCard-userActions with-rightCaret js-userActions">
          <div class="UserActions   UserActions--small u-textLeft">
    <div class="user-actions btn-group following muting can-dm including " data-user-id="18007153" data-screen-name="matt_klein" data-name="Matt Klein" data-protected="false">
      <span class="UserActions-moreActions u-inlineBlock">
          <button type="button" class="js-tooltip unmute-button btn small plain-btn" title="Unmute @matt_klein" data-placement="top">
            <span class="Icon Icon--muted Icon--medium"><span class="visuallyhidden">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span></span>
          </button><button type="button" class="first-load js-tooltip mute-button btn small plain-btn" title="Mute @matt_klein" data-placement="top">
            <span class="Icon Icon--unmuted Icon--medium"><span class="visuallyhidden">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span></span>
          </button></span><span class="user-actions-follow-button js-follow-btn follow-button">
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    follow-text">
      <span aria-hidden="true">Follow</span>
      <span class="u-hiddenVisually">Follow <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--primary
    EdgeButton--small 
    
    button-text
    following-text">
      <span aria-hidden="true">Following</span>
      <span class="u-hiddenVisually">Following <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unfollow-text">
      <span aria-hidden="true">Unfollow</span>
      <span class="u-hiddenVisually">Unfollow <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--invertedDanger
    EdgeButton--small 
    
    button-text
    blocked-text">
    <span aria-hidden="true">Blocked</span>
    <span class="u-hiddenVisually">Blocked <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unblock-text">
    <span aria-hidden="true">Unblock</span>
    <span class="u-hiddenVisually">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    pending-text">
    <span aria-hidden="true">Pending</span>
    <span class="u-hiddenVisually">Pending follow request from <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    cancel-text">
    <span aria-hidden="true">Cancel</span>
    <span class="u-hiddenVisually">Cancel your follow request to <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></span>
  </button>
</span>

<div class="dropdown ">
  <button type="button" class="user-dropdown dropdown-toggle js-dropdown-toggle js-link js-tooltip btn plain-btn small-user-dropdown" title="More user actions" aria-haspopup="true">
    <span class="user-dropdown-icon Icon Icon--dotsVertical Icon--small"><span class="visuallyhidden">User actions</span></span>
  </button>
  <div class="dropdown-menu dropdown-menu--rightAlign is-autoCentered is-forceRight">
    <div class="dropdown-caret">
      <span class="caret-outer"></span>
      <span class="caret-inner"></span>
    </div>
    <ul>
      <li class="mention-text not-blocked"><button type="button" class="dropdown-link">Tweet to <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></button></li>
      <li class="dm-text"><button type="button" class="dropdown-link">Send a Direct Message</button></li>
      <li class="list-text not-blocked"><button type="button" class="dropdown-link">Add or remove from lists…</button></li>
      <li class="dropdown-divider not-blocked"></li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></button></li>

        <li class="block-text not-blocked"><button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></button></li>
        <li class="unblock-text"><button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></button></li>
        <li class="report-text"><button type="button" class="dropdown-link">Report <span class="username u-dir u-textTruncate" dir="ltr">@<b>matt_klein</b></span></button></li>
      <li class="hide-suggestion-text"><button type="button" class="dropdown-link">Hide this suggestion</button></li>
      <li class="dropdown-divider is-following"></li>
      <li class="retweet-on-text"><button type="button" class="dropdown-link">Turn on Retweets</button></li>
      <li class="retweet-off-text"><button type="button" class="dropdown-link">Turn off Retweets</button></li>
      <li class="device-notifications-on-text"><button type="button" class="dropdown-link">Turn on mobile notifications</button></li>
      <li class="device-notifications-off-text"><button type="button" class="dropdown-link">Turn off mobile notifications</button></li>
      <li class="dropdown-divider is-embeddable"></li>
      <li class="embed-profile"><button type="button" class="dropdown-link">Embed this Profile</button></li>
    </ul>
  </div>
</div>

    </div>
</div>

        </div>
      </div>

    <div class="ProfileCard-userFields">
      <div class="ProfileNameTruncated account-group">
  <div class="u-textTruncate u-inlineBlock">
    <a class="fullname ProfileNameTruncated-link u-textInheritColor js-nav" href="/matt_klein" data-aria-label-part="">
      Matt Klein</a></div><span class="UserBadges"></span>
</div>
      
      <span class="ProfileCard-screenname">
        <a href="/matt_klein" class="ProfileCard-screennameLink u-linkComplex js-nav" data-aria-label-part="">
          <span class="username u-dir" dir="ltr">@<b class="u-linkComplex-target">matt_klein</b></span>
        </a><span>‏</span> <span class="FollowStatus">Follows you</span>
      </span>
      
      <p class="ProfileCard-bio u-dir" dir="ltr" data-aria-label-part="">Advisor &amp; Product at Blue Owl - formerly Head of Product at PIX System, Dwell &amp; Yahoo! Travel. Whiteboarder, photographer &amp; provoker of new…</p>
      


    </div>
  </div>
</div>
"""

NOT_MUTED_CARD = """
<div class="ProfileCard js-actionable-user
    " data-screen-name="mattsmollinger" data-user-id="15635001" data-feedback-token="" data-impression-id="">
  <a class="ProfileCard-bg js-nav" href="/mattsmollinger" tabindex="-1" aria-hidden="true" style="
    background-color: #0084B4;
    background-image: url(https://pbs.twimg.com/profile_banners/15635001/1363699398/600x200);">
  </a>

  <div class="ProfileCard-content">
    <a class="ProfileCard-avatarLink js-nav js-tooltip" href="/mattsmollinger" title="Matt Smollinger" tabindex="-1" aria-hidden="true">
      <img class="ProfileCard-avatarImage js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/794270740916928516/8wbnJidA_bigger.jpg" alt="">
    </a>
    
      <div class="ProfileCard-actions">
        <div class="ProfileCard-userActions with-rightCaret js-userActions">
          <div class="UserActions   UserActions--small u-textLeft">
    <div class="user-actions btn-group following not-muting can-dm including " data-user-id="15635001" data-screen-name="mattsmollinger" data-name="Matt Smollinger" data-protected="false">
      <span class="UserActions-moreActions u-inlineBlock">
          <button type="button" class="js-tooltip unmute-button btn small plain-btn" title="Unmute @mattsmollinger" data-placement="top">
            <span class="Icon Icon--muted Icon--medium"><span class="visuallyhidden">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span></span>
          </button><button type="button" class="first-load js-tooltip mute-button btn small plain-btn" title="Mute @mattsmollinger" data-placement="top">
            <span class="Icon Icon--unmuted Icon--medium"><span class="visuallyhidden">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span></span>
          </button></span><span class="user-actions-follow-button js-follow-btn follow-button">
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    follow-text">
      <span aria-hidden="true">Follow</span>
      <span class="u-hiddenVisually">Follow <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--primary
    EdgeButton--small 
    
    button-text
    following-text">
      <span aria-hidden="true">Following</span>
      <span class="u-hiddenVisually">Following <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unfollow-text">
      <span aria-hidden="true">Unfollow</span>
      <span class="u-hiddenVisually">Unfollow <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--invertedDanger
    EdgeButton--small 
    
    button-text
    blocked-text">
    <span aria-hidden="true">Blocked</span>
    <span class="u-hiddenVisually">Blocked <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unblock-text">
    <span aria-hidden="true">Unblock</span>
    <span class="u-hiddenVisually">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    pending-text">
    <span aria-hidden="true">Pending</span>
    <span class="u-hiddenVisually">Pending follow request from <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    cancel-text">
    <span aria-hidden="true">Cancel</span>
    <span class="u-hiddenVisually">Cancel your follow request to <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></span>
  </button>
</span>

<div class="dropdown ">
  <button type="button" class="user-dropdown dropdown-toggle js-dropdown-toggle js-link js-tooltip btn plain-btn small-user-dropdown" title="More user actions" aria-haspopup="true">
    <span class="user-dropdown-icon Icon Icon--dotsVertical Icon--small"><span class="visuallyhidden">User actions</span></span>
  </button>
  <div class="dropdown-menu dropdown-menu--rightAlign is-autoCentered is-forceRight">
    <div class="dropdown-caret">
      <span class="caret-outer"></span>
      <span class="caret-inner"></span>
    </div>
    <ul>
      <li class="mention-text not-blocked"><button type="button" class="dropdown-link">Tweet to <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></button></li>
      <li class="dm-text"><button type="button" class="dropdown-link">Send a Direct Message</button></li>
      <li class="list-text not-blocked"><button type="button" class="dropdown-link">Add or remove from lists…</button></li>
      <li class="dropdown-divider not-blocked"></li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></button></li>

        <li class="block-text not-blocked"><button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></button></li>
        <li class="unblock-text"><button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></button></li>
        <li class="report-text"><button type="button" class="dropdown-link">Report <span class="username u-dir u-textTruncate" dir="ltr">@<b>mattsmollinger</b></span></button></li>
      <li class="hide-suggestion-text"><button type="button" class="dropdown-link">Hide this suggestion</button></li>
      <li class="dropdown-divider is-following"></li>
      <li class="retweet-on-text"><button type="button" class="dropdown-link">Turn on Retweets</button></li>
      <li class="retweet-off-text"><button type="button" class="dropdown-link">Turn off Retweets</button></li>
      <li class="device-notifications-on-text"><button type="button" class="dropdown-link">Turn on mobile notifications</button></li>
      <li class="device-notifications-off-text"><button type="button" class="dropdown-link">Turn off mobile notifications</button></li>
      <li class="dropdown-divider is-embeddable"></li>
      <li class="embed-profile"><button type="button" class="dropdown-link">Embed this Profile</button></li>
    </ul>
  </div>
</div>

    </div>
</div>

        </div>
      </div>

    <div class="ProfileCard-userFields">
      <div class="ProfileNameTruncated account-group">
  <div class="u-textTruncate u-inlineBlock">
    <a class="fullname ProfileNameTruncated-link u-textInheritColor js-nav" href="/mattsmollinger" data-aria-label-part="">
      Matt Smollinger</a></div><span class="UserBadges"></span>
</div>
      
      <span class="ProfileCard-screenname">
        <a href="/mattsmollinger" class="ProfileCard-screennameLink u-linkComplex js-nav" data-aria-label-part="">
          <span class="username u-dir" dir="ltr">@<b class="u-linkComplex-target">mattsmollinger</b></span>
        </a><span>‏</span> <span class="FollowStatus">Follows you</span>
      </span>
      
      <p class="ProfileCard-bio u-dir" dir="ltr" data-aria-label-part="">Head of Mobile <a href="/Mapzen" class="tweet-url twitter-atreply pretty-link" dir="ltr" data-mentioned-user-id="0" rel="nofollow"><s>@</s><b>Mapzen</b></a>, Mobile Dev, and general geek.</p>
      


    </div>
  </div>
</div>
"""
def test_username():
  card = ParseCard(CARD)
  assert card.name == 'Matt Klein'

def test_twitterhandle():
  card = ParseCard(CARD)
  assert card.twitter_handle == '@matt_klein'

def test_muted():
  card = ParseCard(CARD)
  assert card.muted == True

def test_notmuted():
  card = ParseCard(NOT_MUTED_CARD)
  assert card.muted == False
  