import pytest
import context
from datetime import datetime
from twitter_bot.parseprofile import ParseProfile

PROFILE = """
<div id="page-container" class="AppContent">
              
            
  

  
        
<style id="user-style-washingtonpost">






  a,
  a:hover,
  a:focus,
  a:active {
    color: #0057EC;
  }

  .u-textUserColor,
  .u-textUserColorHover:hover,
  .u-textUserColorHover:hover .ProfileTweet-actionCount,
  .u-textUserColorHover:focus {
    color: #0057EC !important;
  }

  .u-borderUserColor,
  .u-borderUserColorHover:hover,
  .u-borderUserColorHover:focus {
    border-color: #0057EC !important;
  }

  .u-bgUserColor,
  .u-bgUserColorHover:hover,
  .u-bgUserColorHover:focus {
    background-color: #0057EC !important;
  }

  .u-dropdownUserColor > li:hover,
  .u-dropdownUserColor > li:focus,
  .u-dropdownUserColor > li > button:hover,
  .u-dropdownUserColor > li > button:focus,
  .u-dropdownUserColor > li > a:focus,
  .u-dropdownUserColor > li > a:hover {
    color: #fff !important;
    background-color: #0057EC !important;
  }

  .u-boxShadowInsetUserColorHover:hover,
  .u-boxShadowInsetUserColorHover:focus {
    box-shadow: inset 0 0 0 5px #0057EC !important;
  }

  .u-dropdownOpenUserColor.dropdown.open .dropdown-toggle {
    color: #0057EC;
  }


  .u-textUserColorLight {
    color: #99BBF7 !important;
  }

  .u-borderUserColorLight,
  .u-borderUserColorLightFocus:focus,
  .u-borderUserColorLightHover:hover,
  .u-borderUserColorLightHover:focus {
    border-color: #99BBF7 !important;
  }

  .u-bgUserColorLight {
    background-color: #99BBF7 !important;
  }


  .u-boxShadowUserColorLighterFocus:focus {
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.05), inset 0 1px 2px rgba(0,87,236,0.25) !important;
  }


  .u-textUserColorLightest {
    color: #E5EEFD !important;
  }

  .u-borderUserColorLightest {
    border-color: #E5EEFD !important;
  }

  .u-bgUserColorLightest {
    background-color: #E5EEFD !important;
  }


  .u-textUserColorLighter {
    color: #BFD5FA !important;
  }

  .u-borderUserColorLighter {
    border-color: #BFD5FA !important;
  }

  .u-bgUserColorLighter {
    background-color: #BFD5FA !important;
  }


  .u-bgUserColorDarkHover:hover {
    background-color: #054DC7 !important;
  }

  .u-borderUserColorDark {
    border-color: #054DC7 !important;
  }


  .u-bgUserColorDarkerActive:active {
    background-color: #0A44A3 !important;
  }













a,
.btn-link,
.btn-link:focus,
.icon-btn,



.pretty-link b,
.pretty-link:hover s,
.pretty-link:hover b,
.pretty-link:focus s,
.pretty-link:focus b,

.metadata a:hover,
.metadata a:focus,

a.account-group:hover .fullname,
a.account-group:focus .fullname,
.account-summary:focus .fullname,

.message .message-text a,
.message .message-text button,
.stats a strong,
.plain-btn:hover,
.plain-btn:focus,
.dropdown.open .user-dropdown.plain-btn,
.open > .plain-btn,
#global-actions .new:before,
.module .list-link:hover,
.module .list-link:focus,

.stats a:hover,
.stats a:hover strong,
.stats a:focus,
.stats a:focus strong,

.find-friends-sources li:hover .source,





.stream-item a:hover .fullname,
.stream-item a:focus .fullname,

.stream-item .view-all-supplements:hover,
.stream-item .view-all-supplements:focus,

.tweet .time a:hover,
.tweet .time a:focus,
.tweet .details.with-icn b,
.tweet .details.with-icn .Icon,

.stream-item:hover .original-tweet .details b,
.stream-item .original-tweet.focus .details b,
.stream-item.open .original-tweet .details b,

.client-and-actions a:hover,
.client-and-actions a:focus,

.dismiss-btn:hover b,

.tweet .context .pretty-link:hover s,
.tweet .context .pretty-link:hover b,
.tweet .context .pretty-link:focus s,
.tweet .context .pretty-link:focus b,

.list .username a:hover,
.list .username a:focus,
.list-membership-container .create-a-list,
.list-membership-container .create-a-list:hover,
.new-tweets-bar,



.card .list-details a:hover,
.card .list-details a:focus,
.card .card-body:hover .attribution,
.card .card-body .attribution:focus {
  color: #0057EC;
}



    #global-actions > li > a {
      border-bottom-color: #0057EC;
    }

    #global-actions > li:hover > a,
    #global-actions > li > a:focus,
    #global-actions > li.active .text,
    .DashUserDropdown.dropdown-menu .nightmode-toggle .Icon,
    .nav.right-actions > li > a:hover,
    .nav.right-actions > li > a:focus {
      color: #0057EC;
    }


  
  .FoundMediaSearch--keyboard .FoundMediaSearch-focusable.is-focused {
    border-color: #0057EC;
  }

  
  .photo-selector:hover .btn,
  .icon-btn:hover,
  .icon-btn:active,
  .icon-btn.active,
  .icon-btn.enabled {
    border-color: #0057EC;
    border-color: rgba(0,87,236,0.4);
    color: #0057EC;
  }

  
  .photo-selector:hover .btn,
  .icon-btn:hover {
    background-image: linear-gradient(rgba(255,255,255,0), rgba(0,87,236,0.1));
  }

  .icon-btn.disabled,
  .icon-btn.disabled:hover,
  .icon-btn[disabled],
  .icon-btn[aria-disabled=true] {
    color: #0057EC;
  }

  
  

  .EdgeButton--primary,
  .EdgeButton--primary:focus {
    background-color: #3278EF;
    border-color: transparent;
  }

  .EdgeButton--primary:hover,
  .EdgeButton--primary:active {
    background-color: #0057EC;
    border-color: #0057EC;
  }

  .EdgeButton--primary:focus {
    box-shadow:
      0 0 0 2px #FFFFFF,
      0 0 0 4px #99BBF7;
  }

  .EdgeButton--primary:active {
    box-shadow:
      0 0 0 2px #FFFFFF,
      0 0 0 4px #3278EF;
  }

  
  

  .EdgeButton--secondary,
  .EdgeButton--secondary:hover,
  .EdgeButton--secondary:focus,
  .EdgeButton--secondary:active {
    border-color: #0057EC;
    color: #0057EC;
  }

  .EdgeButton--secondary:hover,
  .EdgeButton--secondary:active {
    background-color: #E5EEFD;
  }

  .EdgeButton--secondary:focus {
    box-shadow:
      0 0 0 2px #FFFFFF,
      0 0 0 4px rgba(0,87,236,0.4);
  }

  .EdgeButton--secondary:active {
    box-shadow:
      0 0 0 2px #FFFFFF,
      0 0 0 4px #0057EC;
  }

  
  

  .EdgeButton--invertedPrimary {
    color: #0057EC !important;
  }

  .EdgeButton--invertedPrimary:focus {
    box-shadow:
      0 0 0 2px #0057EC,
      0 0 0 4px #99BBF7;
  }

  .EdgeButton--invertedPrimary:active {
    box-shadow:
      0 0 0 2px #0057EC,
      0 0 0 4px #FFFFFF;
  }

  
  

  .EdgeButton--invertedSecondary {
    background-color: #0057EC;
  }

  .EdgeButton--invertedSecondary:hover {
    background-color: #3278EF;
  }

  .EdgeButton--invertedSecondary:focus {
    box-shadow:
      0 0 0 2px #0057EC,
      0 0 0 4px #99BBF7;
  }

  .EdgeButton--invertedSecondary:active {
    box-shadow:
      0 0 0 2px #0057EC,
      0 0 0 4px #FFFFFF;
  }

  

  .btn:focus,
  .btn.focus,
  .Button:focus,
  .EmojiPicker-item.is-focused,
  .EmojiPicker .EmojiCategoryIcon:focus,
  .EmojiPicker-skinTone:focus + .EmojiPicker-skinToneSwatch,
  a:focus > img:first-child:last-child,
  button:focus {
    box-shadow:
      0 0 0 2px #FFFFFF,
      0 0 2px 4px rgba(0,87,236,0.4);
  }

  .selected-stream-item:focus {
    box-shadow: 0 0 0 3px rgba(0,87,236,0.4);
  }

  
  .js-navigable-stream.stream-table-view .selected-stream-item[tabindex="-1"]:focus {
    outline: 3px solid rgba(0,87,236,0.4) !important;
  }

  
  .js-navigable-stream.stream-table-view .selected-stream-item:focus {
    box-shadow: none;
  }

  

  .global-dm-nav.new.with-count .dm-new .count-inner {
    background: #0057EC;
  }

  .global-nav .people .count .count-inner {
    background: #0057EC;
  }

  .dropdown-menu li > a:hover,
  .dropdown-menu li > a:focus,
  .dropdown-menu .dropdown-link:hover,
  .dropdown-menu .dropdown-link:focus,
  .dropdown-menu .dropdown-link.is-focused,
  .dropdown-menu li:hover .dropdown-link,
  .dropdown-menu li:focus .dropdown-link,
  .dropdown-menu .selected a,
  .dropdown-menu .dropdown-link.selected {
    background-color: #0057EC !important;
  }

  /* for items in typeahead dropdown menu on logged in pages */
  .dropdown-menu .typeahead-items li > a:focus,
  .dropdown-menu .typeahead-items li > a:hover,
  .dropdown-menu .typeahead-items .selected,
  .dropdown-menu .typeahead-items .selected a {
    background-color: #E5EEFD !important;
    color: #0057EC !important;
  }

  .typeahead a:hover,
  .typeahead a:hover strong,
  .typeahead a:hover .fullname,
  .typeahead .selected a,
  .typeahead .selected strong,
  .typeahead .selected .fullname,
  .typeahead .selected .Icon--close {
    color: #0057EC !important;
  }


.home-tweet-box,
.LiveVideo-tweetBox,
.RetweetDialog-commentBox {
  background-color: #E5EEFD;
}

.top-timeline-tweetbox .timeline-tweet-box .tweet-form.condensed .tweet-box {
  color: #0057EC;
}

.RichEditor,
.TweetBoxAttachments {
  border-color: #BFD5FA;
}

input:focus,
textarea:focus,
div[contenteditable="true"]:focus,
div[contenteditable="true"].fake-focus,
div[contenteditable="plaintext-only"]:focus,
div[contenteditable="plaintext-only"].fake-focus {
  border-color: #99BBF7;
  box-shadow: inset 0 0 0 1px rgba(0,87,236,0.7);
}

.tweet-box textarea:focus,
.tweet-box input[type=text],
.currently-dragging .tweet-form.is-droppable .tweet-drag-help,
.tweet-box[contenteditable="true"]:focus,
.RichEditor.is-fakeFocus,
.RichEditor.is-fakeFocus ~ .TweetBoxAttachments {
  border-color: #99BBF7;
  box-shadow: 0 0 0 1px #99BBF7;
}

.MomentCapsuleItem.selected-stream-item:focus {
  box-shadow: 0 0 0 3px rgba(0,87,236,0.4);
}




s,
.pretty-link:hover s,
.pretty-link:focus s,
.stream-item-activity-notification .latest-tweet .tweet-row a:hover s,
.stream-item-activity-notification .latest-tweet .tweet-row a:focus s {
    color: #0057EC;
}



.vellip,
.vellip:before,
.vellip:after,
.conversation-module > li:after,
.conversation-module > li:before,
.ThreadedConversation--loneTweet:after,
.ThreadedConversation-tweet:not(.is-hiddenAncestor) ~ .ThreadedConversation-tweet:before,
.ThreadedConversation-tweet:after,
.ThreadedConversation-moreReplies:before,
.ThreadedConversation-viewOther:before,
.ThreadedConversation-unavailableTweet:before,
.ThreadedConversation-unavailableTweet:after,
.ThreadedConversation--permalinkTweetWithAncestors:before,
.mini-avatar-with-thread:before,
.permalink.self-thread-permalink-with-descendant .permalink-tweet-container:after,
.permalink.self-thread-permalink-with-descendant .inline-reply-tweetbox-container:after {
    border-color: #99BBF7;
}




.tweet .sm-reply,
.tweet .sm-rt,
.tweet .sm-fav,
.tweet .sm-image,
.tweet .sm-video,
.tweet .sm-audio,
.tweet .sm-geo,
.tweet .sm-in,
.tweet .sm-trash,
.tweet .sm-more,
.tweet .sm-page,
.tweet .sm-embed,
.tweet .sm-summary,
.tweet .sm-chat,

.timelines-navigation .active .profile-nav-icon,
.timelines-navigation .profile-nav-icon:hover,
.timelines-navigation .profile-nav-link:focus .profile-nav-icon,

.sm-top-tweet {
    background-color: #0057EC;
}

.enhanced-mini-profile .mini-profile .profile-summary {
  background-image: url(https://pbs.twimg.com/profile_banners/2467791/1469484132/mobile);
}

  #global-tweet-dialog .modal-header,
  #Tweetstorm-dialog .modal-header {
    border-bottom: solid 1px rgba(0,87,236,0.25);
  }

  #global-tweet-dialog .modal-tweet-form-container,
  #Tweetstorm-dialog .modal-body {
    background-color: #0057EC;
    background: rgba(0,87,236,0.1);
  }

  .TweetstormDialog-reply-context .tweet-box-avatar:after,
  .TweetstormDialog-reply-context .tweet-box-avatar:before,
  .TweetstormDialog-tweet-box .tweet-box-avatar:after,
  .TweetstormDialog-tweet-box .tweet-box-avatar:before {
    border-color: #99BBF7;
  }

  .global-nav .search-input:focus,
  .global-nav .search-input.focus {
    border: 2px solid #0057EC;
  }
}

  .inline-reply-tweetbox {
    background-color: #E5EEFD;
  }

</style>


    <div class="ProfileCanopy ProfileCanopy--withNav ProfileCanopy--large js-variableHeightTopBar">
  <div class="ProfileCanopy-inner">

    <div class="ProfileCanopy-header u-bgUserColor" style="margin-top: 0px;">
  <div class="ProfileCanopy-headerBg">
    <img alt="" src="https://pbs.twimg.com/profile_banners/2467791/1469484132/1500x500" style="transform: none;">
  </div>

  <div class="AppContainer">

    <div class="ProfileCanopy-avatar">
      <div class="ProfileAvatar">
    <a class="ProfileAvatar-container u-block js-tooltip profile-picture" href="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_400x400.jpg" title="Washington Post" data-resolved-url-large="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_400x400.jpg" data-url="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_400x400.jpg" target="_blank" rel="noopener">
        <img class="ProfileAvatar-image " src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_400x400.jpg" alt="Washington Post">
    </a>
</div>

    </div>


    <div class="ProfileCanopy-headerPromptAnchor"></div>
  </div>

</div>


    <div class="ProfileCanopy-navBar u-boxShadow">
      
      <div class="AppContainer">
        <div class="Grid Grid--withGutter">
          <div class="Grid-cell u-size1of3 u-lg-size1of4">
            <div class="ProfileCanopy-card" role="presentation" aria-hidden="true">
              <div class="ProfileCardMini">
  <a class="ProfileCardMini-avatar profile-picture js-tooltip" href="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO.jpg" title="Washington Post" data-resolved-url-large="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO.jpg" data-url="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO.jpg" target="_blank" rel="noopener" tabindex="-1">
    <img class="ProfileCardMini-avatarImage" alt="Washington Post" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_normal.jpg">
  </a>
  <div class="ProfileCardMini-details">
    <div class="ProfileNameTruncated account-group">
  <div class="u-textTruncate u-inlineBlock ProfileNameTruncated-withBadges ProfileNameTruncated-withBadges--1">
    <a class="fullname ProfileNameTruncated-link u-textInheritColor js-nav" href="/washingtonpost" data-aria-label-part="" tabindex="-1">
      Washington Post</a></div><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span>
</div>
    <div class="ProfileCardMini-screenname">
      <a href="/washingtonpost" class="ProfileCardMini-screennameLink u-linkComplex js-nav u-dir" dir="ltr" tabindex="-1">
        <span class="username u-dir" dir="ltr">@<b class="u-linkComplex-target">washingtonpost</b></span>
      </a>
    </div>
  </div>
</div>

            </div>
          </div>

          <div class="Grid-cell u-size2of3 u-lg-size3of4">
            <div class="ProfileCanopy-nav">
              
  <div class="ProfileNav" role="navigation" data-user-id="2467791">
    <ul class="ProfileNav-list">
<li class="ProfileNav-item ProfileNav-item--tweets is-active" style="">
          <a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav" data-nav="tweets" tabindex="0" data-original-title="271,548 Tweets">
            <span class="ProfileNav-label" aria-hidden="true">Tweets</span>
              <span class="u-hiddenVisually">Tweets, current page.</span>
            <span class="ProfileNav-value" data-count="271548" data-is-compact="true">272K
            </span>
          </a>
        </li><li class="ProfileNav-item ProfileNav-item--following" style="">
        <a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav u-textUserColor" data-nav="following" href="/washingtonpost/following" data-original-title="1,479 Following">
          <span class="ProfileNav-label" aria-hidden="true">Following</span>
            <span class="u-hiddenVisually">Following</span>
          <span class="ProfileNav-value" data-count="1479" data-is-compact="false">1,479</span>
        </a>
      </li><li class="ProfileNav-item ProfileNav-item--followers" style="">
        <a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav u-textUserColor" title="12,598,791 Followers" data-nav="followers" href="/washingtonpost/followers">
          <span class="ProfileNav-label" aria-hidden="true">Followers</span>
            <span class="u-hiddenVisually">Followers</span>
          <span class="ProfileNav-value" data-count="12598791" data-is-compact="true">12.6M</span>
        </a>
      </li><li class="ProfileNav-item ProfileNav-item--favorites" data-more-item=".ProfileNav-dropdownItem--favorites" style="">
        <a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav u-textUserColor" title="4,496 Likes" data-nav="favorites" href="/washingtonpost/likes">
          <span class="ProfileNav-label" aria-hidden="true">Likes</span>
            <span class="u-hiddenVisually">Likes</span>
          <span class="ProfileNav-value" data-count="4496" data-is-compact="false">4,496</span>
        </a>
      </li><li class="ProfileNav-item ProfileNav-item--lists" data-more-item=".ProfileNav-dropdownItem--lists" style="">
        <a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip  js-nav u-textUserColor" title="30 Lists" data-nav="all_lists" href="/washingtonpost/lists">
          <span class="ProfileNav-label" aria-hidden="true">Lists</span>
            <span class="u-hiddenVisually">Lists</span>
          <span class="ProfileNav-value" data-is-compact="false">30</span>
        </a></li><li class="ProfileNav-item ProfileNav-item--moments" data-more-item=".ProfileNav-dropdownItem--userMoments" style="">
        <a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav u-textUserColor" data-nav="user_moments" href="/washingtonpost/moments" data-original-title="31 Moments">
          <span class="ProfileNav-label" aria-hidden="true">Moments</span>
            <span class="u-hiddenVisually">Moments</span>
          <span class="ProfileNav-value" data-is-compact="false">31</span>
        </a></li><li class="ProfileNav-item ProfileNav-item--more dropdown is-hidden" style="">        <a class="ProfileNav-stat ProfileNav-stat--link ProfileNav-stat--moreLink js-dropdown-toggle" role="button" href="#more" aria-haspopup="true">
          <span class="ProfileNav-label">&nbsp;</span>
          <span class="ProfileNav-value">More <span class="ProfileNav-dropdownCaret Icon Icon--medium Icon--caretDown"></span></span>
        </a>
        <div class="dropdown-menu">
          <div class="dropdown-caret">
            <span class="caret-outer"></span>
            <span class="caret-inner"></span>
          </div>
          <ul><li>
              <a href="/washingtonpost/likes" class="ProfileNav-dropdownItem ProfileNav-dropdownItem--favorites is-hidden u-bgUserColorHover u-bgUserColorFocus u-linkClean js-nav" style="">Likes</a></li><li>
              <a href="/washingtonpost/lists" class="ProfileNav-dropdownItem ProfileNav-dropdownItem--lists is-hidden u-bgUserColorHover u-bgUserColorFocus u-linkClean js-nav" style="">Lists</a></li><li>
              <a href="/washingtonpost/moments" class="ProfileNav-dropdownItem ProfileNav-dropdownItem--userMoments is-hidden u-bgUserColorHover u-bgUserColorFocus u-linkClean js-nav" style="">Moments</a></li></ul>
        </div>
      </li><li class="ProfileNav-item ProfileNav-item--userActions u-floatRight u-textRight with-rightCaret " style="">
        <div class="UserActions   u-textLeft">
    <div class="user-actions btn-group not-following not-muting " data-user-id="2467791" data-screen-name="washingtonpost" data-name="Washington Post" data-protected="false">
      <span class="UserActions-moreActions u-inlineBlock">
          <button type="button" class="js-tooltip unmute-button btn small plain-btn" title="Unmute @washingtonpost" data-placement="top">
            <span class="Icon Icon--muted Icon--medium"><span class="visuallyhidden">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span></span>
          </button><button type="button" class="first-load js-tooltip mute-button btn small plain-btn" title="Mute @washingtonpost" data-placement="top">
            <span class="Icon Icon--unmuted Icon--medium"><span class="visuallyhidden">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span></span>
          </button></span><span class="user-actions-follow-button js-follow-btn follow-button">
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    
    EdgeButton--medium 
    button-text
    follow-text">
      <span aria-hidden="true">Follow</span>
      <span class="u-hiddenVisually">Follow <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--primary
    
    EdgeButton--medium 
    button-text
    following-text">
      <span aria-hidden="true">Following</span>
      <span class="u-hiddenVisually">Following <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    
    EdgeButton--medium 
    button-text
    unfollow-text">
      <span aria-hidden="true">Unfollow</span>
      <span class="u-hiddenVisually">Unfollow <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--invertedDanger
    
    EdgeButton--medium 
    button-text
    blocked-text">
    <span aria-hidden="true">Blocked</span>
    <span class="u-hiddenVisually">Blocked <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    
    EdgeButton--medium 
    button-text
    unblock-text">
    <span aria-hidden="true">Unblock</span>
    <span class="u-hiddenVisually">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    
    EdgeButton--medium 
    button-text
    pending-text">
    <span aria-hidden="true">Pending</span>
    <span class="u-hiddenVisually">Pending follow request from <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    
    EdgeButton--medium 
    button-text
    cancel-text">
    <span aria-hidden="true">Cancel</span>
    <span class="u-hiddenVisually">Cancel your follow request to <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></span>
  </button>
</span>

<div class="dropdown ">
  <button type="button" class="user-dropdown dropdown-toggle js-dropdown-toggle js-link js-tooltip btn plain-btn" aria-haspopup="true" data-original-title="More user actions">
    <span class="user-dropdown-icon Icon Icon--dotsVertical Icon--medium"><span class="visuallyhidden">User actions</span></span>
  </button>
  <div class="dropdown-menu dropdown-menu--rightAlign is-autoCentered is-forceRight">
    <div class="dropdown-caret">
      <span class="caret-outer"></span>
      <span class="caret-inner"></span>
    </div>
    <ul>
      <li class="mention-text not-blocked"><button type="button" class="dropdown-link">Tweet to <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
      <li class="dm-text"><button type="button" class="dropdown-link">Send a Direct Message</button></li>
      <li class="list-text not-blocked"><button type="button" class="dropdown-link">Add or remove from lists…</button></li>
      <li class="dropdown-divider not-blocked"></li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-text not-blocked"><button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
        <li class="unblock-text"><button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
        <li class="report-text"><button type="button" class="dropdown-link">Report <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
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

      </li>
    </ul>
  </div>

            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>



    <div class="AppContainer">
      <div class="AppContent-main content-main u-cf" role="main" aria-labelledby="content-main-heading">
        <div class="Grid Grid--withGutter">
          <div class="Grid-cell u-size1of3 u-lg-size1of4">
            <div class="Grid Grid--withGutter">
              <div class="Grid-cell">
                <div class="ProfileSidebar ProfileSidebar--withLeftAlignment">
  <div class="ProfileHeaderCard">
  <h1 class="ProfileHeaderCard-name">
    <a href="/washingtonpost" class="ProfileHeaderCard-nameLink u-textInheritColor js-nav">Washington Post</a><span class="ProfileHeaderCard-badges"><a href="/help/verified" class="js-tooltip" target="_blank" title="Verified account" data-placement="right" rel="noopener"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></a></span>
  </h1>

  <h2 class="ProfileHeaderCard-screenname u-inlineBlock u-dir" dir="ltr">
    <a class="ProfileHeaderCard-screennameLink u-linkComplex js-nav" href="/washingtonpost">
      <span class="username u-dir" dir="ltr">@<b class="u-linkComplex-target">washingtonpost</b></span>
    </a>
  </h2>

  

      <p class="ProfileHeaderCard-bio u-dir" dir="ltr">Tweet-length breaking news, analysis from around the world. Founded in 1877. Follow our journalists on Twitter: <a href="https://t.co/VV0UBAMHg8" rel="nofollow noopener" dir="ltr" data-expanded-url="https://twitter.com/washingtonpost/lists/washington-post-people" class="twitter-timeline-link" target="_blank" title="https://twitter.com/washingtonpost/lists/washington-post-people"><span class="invisible">https://</span><span class="js-display-url">twitter.com/washingtonpost</span><span class="invisible">/lists/washington-post-people</span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span>…</span></a></p>

      <div class="ProfileHeaderCard-location ">
        <span class="Icon Icon--geo Icon--medium" aria-hidden="true" role="presentation"></span>
        <span class="ProfileHeaderCard-locationText u-dir" dir="ltr">
              <a href="/search?q=place%3A01fbe706f872cb32" data-place-id="01fbe706f872cb32">Washington, DC</a>

        </span>
      </div>

      <div class="ProfileHeaderCard-url ">
        <span class="Icon Icon--url Icon--medium" aria-hidden="true" role="presentation"></span>
        <span class="ProfileHeaderCard-urlText u-dir">  <a class="u-textUserColor" target="_blank" rel="me nofollow noopener" href="http://t.co/Hq7hTYkOPg" title="http://washingtonpost.com">
    washingtonpost.com
  </a>

</span>
      </div>


      <div class="ProfileHeaderCard-joinDate">
        <span class="Icon Icon--calendar Icon--medium" aria-hidden="true" role="presentation"></span>
        <span class="ProfileHeaderCard-joinDateText js-tooltip u-dir" dir="ltr" title="7:19 AM - 27 Mar 2007">Joined March 2007</span>
      </div>

      <div class="ProfileHeaderCard-birthdate u-hidden">
        <span class="Icon Icon--balloon Icon--medium" aria-hidden="true" role="presentation"></span>
        <span class="ProfileHeaderCard-birthdateText u-dir" dir="ltr">
</span>
      </div>


          <div class="ProfileMessagingActions">
  <div class="ProfileMessagingActions-actionsContainer">
<div class="ProfileMessagingActions-buttonWrapper u-sizeFull">
      <button class="NewTweetButton u-sizeFull js-tooltip EdgeButton EdgeButton--primary u-textTruncate" type="button" data-draft-tweet-id="profile_2467791" data-dialog-title="Tweet to Washington Post" data-screen-name="washingtonpost" data-original-title="Tweet to Washington Post">
  <span class="NewTweetButton-content button-text tweeting-text">
    <span class="NewTweetButton-text" aria-hidden="true">Tweet to Washington Post</span><span class="u-hiddenVisually">Mention Washington Post in a Tweet</span>
  </span>
</button>

    </div>  </div>
</div>

</div>




      <div class="ProfileUserList ProfileUserList--socialProof">
  <div class="ProfileUserList-heading">
    <div class="ProfileUserList-title">
      <span class="Icon Icon--person Icon--medium" aria-hidden="true" role="presentation"></span>
      <span class="ProfileUserList-listName">
            <a href="/washingtonpost/followers_you_follow" class="ProfileUserList-permalink u-textUserColor js-nav">144 Followers you know</a>
      </span>
    </div>
  </div>
  <ul class="ProfileUserList-facepile u-cf">
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/g_philip" data-user-id="75796430" original-title="Philip Rogers" title="Philip Rogers" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/853989973955035136/cC84MIE4_bigger.jpg" alt="Philip Rogers">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/stephneumann" data-user-id="21168037" original-title="Stephanie Neumann" title="Stephanie Neumann" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/378800000163404787/ac19a88a86cdc6ed1360485f005c8493_bigger.jpeg" alt="Stephanie Neumann">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/AVasilevskis" data-user-id="3364581" original-title="Alissa Vasilevskis" title="Alissa Vasilevskis" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/3151206197/286892a96112c6e8a43aad664cf8450d_bigger.jpeg" alt="Alissa Vasilevskis">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/kavyabanavar" data-user-id="1659900408" original-title="Kavya Banavar" title="Kavya Banavar" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/845605701531533312/z9yz04uL_bigger.jpg" alt="Kavya Banavar">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/NikLaCroce" data-user-id="885117834" original-title="Nikki La Croce" title="Nikki La Croce" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/824665907561697281/HmyKtoKy_bigger.jpg" alt="Nikki La Croce">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/danieltramacchi" data-user-id="241067822" original-title="Daniel Tramacchi" title="Daniel Tramacchi" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/750497475404771329/x1bCk3Od_bigger.jpg" alt="Daniel Tramacchi">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/narendrajee" data-user-id="189281530" original-title="Narendra Yadav" title="Narendra Yadav" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/771030516728532992/8ScStCRX_bigger.jpg" alt="Narendra Yadav">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/jkmaderic" data-user-id="241078057" original-title="Jason Maderic" title="Jason Maderic" data-nav="avatar">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/614889414846730242/P982DN1p_bigger.jpg" alt="Jason Maderic">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/FutureheadsProd" data-user-id="2687630768" original-title="Futureheads Product" data-nav="avatar" data-original-title="Futureheads Product">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/687981873755193344/PsQQHXOO_bigger.png" alt="Futureheads Product">
</a>

      </li>
      <li class="ProfileUserList-facepileItem">
        <a class="u-block js-tooltip js-nav" href="/rks" data-user-id="50820551" original-title="RKS Design" data-nav="avatar" data-original-title="RKS Design">
  <img class="Avatar Avatar--size48" src="https://pbs.twimg.com/profile_images/999040101526065153/nLCb9Z8r_bigger.jpg" alt="RKS Design">
</a>

      </li>
  </ul>
</div>


      <div class="PhotoRail" style="display: block;" data-loaded="true">
  <div class="PhotoRail-heading">
    <span class="Icon Icon--camera Icon--medium" aria-hidden="true" role="presentation"></span>
    <span class="PhotoRail-headingText PhotoRail-headingText--withCount">
            <a href="/washingtonpost/media" class="PhotoRail-headingWithCount js-nav">
                
                13.5K Photos and videos
            </a>
          <a href="/washingtonpost/media" class="PhotoRail-headingWithoutCount js-nav">
            Photos and videos
          </a>
    </span>
  </div>
  <div class="PhotoRail-mediaBox">
    <span class="tweet-media-img-placeholder js-nav" data-status-id="1002313291140599808" data-image-url="https://pbs.twimg.com/media/DejuoFgX4AEhqbB.jpg" data-img-alt="" data-load-status="loaded" background-color="style: rgba(42,50,64,1.0)" data-dominant-color="[42,50,64]" data-tweet-id="1002313291140599808" data-item-id="1002313291140599808" data-permalink-path="/washingtonpost/status/1002313291140599808" data-conversation-id="1002313291140599808" data-tweet-nonce="1002313291140599808-6b90444f-ded6-4b93-b903-035e49936e10" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    <img src="https://pbs.twimg.com/media/DejuoFgX4AEhqbB.jpg:thumb" style="height: 83px; width: 83px; margin-left: 0px; margin-top: 0px;" alt=""></span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="1002270767042781186" data-image-url="https://pbs.twimg.com/media/DejH81_WsAM0WeB.jpg" data-img-alt="" data-load-status="loaded" background-color="style: rgba(64,25,47,1.0)" data-dominant-color="[64,25,47]" data-tweet-id="1002270767042781186" data-item-id="1002270767042781186" data-permalink-path="/washingtonpost/status/1002270767042781186" data-conversation-id="1002270767042781186" data-tweet-nonce="1002270767042781186-7bf5c396-e094-4cd6-9b4b-158180429beb" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    <img src="https://pbs.twimg.com/media/DejH81_WsAM0WeB.jpg:thumb" style="height: 83px; width: 83px; margin-left: 0px; margin-top: 0px;" alt=""></span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="1001990906101280769" data-image-url="https://pbs.twimg.com/media/DefJazvXkAIauit.jpg" data-img-alt="" data-load-status="loaded" background-color="style: rgba(38,27,33,1.0)" data-dominant-color="[38,27,33]" data-tweet-id="1001990906101280769" data-item-id="1001990906101280769" data-permalink-path="/washingtonpost/status/1001990906101280769" data-conversation-id="1001990906101280769" data-tweet-nonce="1001990906101280769-540af446-1345-4b21-a11e-c2ab00abf86f" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    <img src="https://pbs.twimg.com/media/DefJazvXkAIauit.jpg:thumb" style="height: 83px; width: 83px; margin-left: 0px; margin-top: 0px;" alt=""></span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="1001486856100474880" data-image-url="https://pbs.twimg.com/media/DeX-_O_XkAErBIY.jpg" data-img-alt="" data-load-status="loaded" background-color="style: rgba(38,27,21,1.0)" data-dominant-color="[38,27,21]" data-tweet-id="1001486856100474880" data-item-id="1001486856100474880" data-permalink-path="/washingtonpost/status/1001486856100474880" data-conversation-id="1001486856100474880" data-tweet-nonce="1001486856100474880-7285894b-8684-4690-9405-0329abda5aad" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    <img src="https://pbs.twimg.com/media/DeX-_O_XkAErBIY.jpg:thumb" style="height: 83px; width: 83px; margin-left: 0px; margin-top: 0px;" alt=""></span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="1000063728442904576" data-image-url="https://pbs.twimg.com/media/DeDwqSpVAAADBhC.jpg" data-img-alt="" data-load-status="loaded" background-color="style: rgba(22,49,64,1.0)" data-dominant-color="[22,49,64]" data-tweet-id="1000063728442904576" data-item-id="1000063728442904576" data-permalink-path="/washingtonpost/status/1000063728442904576" data-conversation-id="1000063728442904576" data-tweet-nonce="1000063728442904576-caea6a95-f26e-4d50-8818-ec4db265e173" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    <img src="https://pbs.twimg.com/media/DeDwqSpVAAADBhC.jpg:thumb" style="height: 83px; width: 83px; margin-left: 0px; margin-top: 0px;" alt=""></span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="1000043844661071874" data-image-url="https://pbs.twimg.com/media/DeDek2iX0AAsu2_.jpg" data-img-alt="" data-load-status="loaded" background-color="style: rgba(43,32,27,1.0)" data-dominant-color="[43,32,27]" data-tweet-id="1000043844661071874" data-item-id="1000043844661071874" data-permalink-path="/washingtonpost/status/1000043844661071874" data-conversation-id="1000043844661071874" data-tweet-nonce="1000043844661071874-50b39964-9a5e-435c-ac7d-84c0f7445ca3" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    <img src="https://pbs.twimg.com/media/DeDek2iX0AAsu2_.jpg:thumb" style="height: 83px; width: 83px; margin-left: 0px; margin-top: 0px;" alt=""></span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="999063958412824578" data-image-url="https://pbs.twimg.com/media/Dd1eSL_U0AAzzZf.jpg" data-img-alt="" data-load-status="not-loaded" background-color="style: rgba(64,64,64,1.0)" data-dominant-color="[64,64,64]" data-tweet-id="999063958412824578" data-item-id="999063958412824578" data-permalink-path="/washingtonpost/status/999063958412824578" data-conversation-id="999063958412824578" data-tweet-nonce="999063958412824578-11a268cf-cd2b-4d63-85bd-74f459611dd1" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    </span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="997952573339504640" data-image-url="https://pbs.twimg.com/media/DdlwktmVAAAv2BC.jpg" data-img-alt="" data-load-status="not-loaded" background-color="style: rgba(11,51,64,1.0)" data-dominant-color="[11,51,64]" data-tweet-id="997952573339504640" data-item-id="997952573339504640" data-permalink-path="/washingtonpost/status/997952573339504640" data-conversation-id="997952573339504640" data-tweet-nonce="997952573339504640-44b77bb9-cdf2-4cab-ac45-5f7c27daa6e3" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    </span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="997472402517970944" data-image-url="https://pbs.twimg.com/media/Dde73NPVwAAw1Wz.jpg" data-img-alt="" data-load-status="not-loaded" background-color="style: rgba(47,42,39,1.0)" data-dominant-color="[47,42,39]" data-tweet-id="997472402517970944" data-item-id="997472402517970944" data-permalink-path="/washingtonpost/status/997472402517970944" data-conversation-id="997472402517970944" data-tweet-nonce="997472402517970944-d5152aa3-4200-47c9-919a-93d4749e0f8b" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    </span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="997352374606974976" data-image-url="https://pbs.twimg.com/media/DddOsqzVwAEf2Eo.jpg" data-img-alt="" data-load-status="not-loaded" background-color="style: rgba(64,54,13,1.0)" data-dominant-color="[64,54,13]" data-tweet-id="997352374606974976" data-item-id="997352374606974976" data-permalink-path="/washingtonpost/status/997352374606974976" data-conversation-id="997352374606974976" data-tweet-nonce="997352374606974976-9955a886-29e0-4ba9-b115-838af6395d06" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    </span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="997341487967948800" data-image-url="https://pbs.twimg.com/media/DddEzAdXUAAGwZN.jpg" data-img-alt="" data-load-status="not-loaded" background-color="style: rgba(54,64,27,1.0)" data-dominant-color="[54,64,27]" data-tweet-id="997341487967948800" data-item-id="997341487967948800" data-permalink-path="/washingtonpost/status/997341487967948800" data-conversation-id="997341487967948800" data-tweet-nonce="997341487967948800-361b2ca1-9153-4786-ac4b-39bf3b3f3e6d" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    </span>

      <span class="tweet-media-img-placeholder js-nav" data-status-id="997192568852176896" data-image-url="https://pbs.twimg.com/media/Dda9WvhVQAAUwkE.jpg" data-img-alt="" data-load-status="not-loaded" background-color="style: rgba(64,16,10,1.0)" data-dominant-color="[64,16,10]" data-tweet-id="997192568852176896" data-item-id="997192568852176896" data-permalink-path="/washingtonpost/status/997192568852176896" data-conversation-id="997192568852176896" data-tweet-nonce="997192568852176896-89b2b93e-0ab1-4af9-8b42-79ed7f67a175" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-has-cards="true" href="/washingtonpost/media">
      <div class="media-overlay"></div>
    </span><span class="js-photoRailInsertPoint"></span>
  </div>
</div>



</div>

              </div>
            </div>
          </div>

          <div class="Grid-cell u-size2of3 u-lg-size3of4">
            <div class="Grid Grid--withGutter">
                <div class="Grid-cell">
                  <div class="js-profileClusterFollow"></div>
                </div>

              <div class="Grid-cell
                    u-lg-size2of3
              " data-test-selector="ProfileTimeline">
                  
                    <div class="ProfileHeading">
  <div class="ProfileHeading-spacer"></div>
    <div class="ProfileHeading-content">
      <h2 id="content-main-heading" class="ProfileHeading-title u-hiddenVisually ">Tweets</h2>
        <ul class="ProfileHeading-toggle">
            <li class="ProfileHeading-toggleItem  is-active" data-element-term="tweets_toggle">
                <span aria-hidden="true">Tweets</span>
                <span class="u-hiddenVisually">Tweets, current page.</span>
            </li>
            <li class="ProfileHeading-toggleItem  u-textUserColor" data-element-term="tweets_with_replies_toggle">
                <a class="ProfileHeading-toggleLink js-nav" href="/washingtonpost/with_replies" data-nav="tweets_with_replies_toggle">
                  Tweets &amp; replies
                </a>
            </li>
            <li class="ProfileHeading-toggleItem  u-textUserColor" data-element-term="photos_and_videos_toggle">
                <a class="ProfileHeading-toggleLink js-nav" href="/washingtonpost/media" data-nav="photos_and_videos_toggle">
                  Media
                </a>
            </li>
        </ul>
    </div>
</div>

                  <div class="ProfileWarningTimeline" data-element-context="blocked_profile">
  <h2 class="ProfileWarningTimeline-heading" id="content-main-heading">You blocked <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></h2>
  <p class="ProfileWarningTimeline-explanation">Are you sure you want to view these Tweets? Viewing Tweets won't unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></p>
  <button class="EdgeButton EdgeButton--tertiary ProfileWarningTimeline-button">Yes, view profile</button>
</div>
                  




  <div id="scroll-bump-dialog" class="ScrollBumpDialog modal-container">
  <div class="modal draggable">
    <div class="modal-content clearfix">

      <button type="button" class="modal-btn modal-close js-close">
  <span class="Icon Icon--close Icon--medium">
    <span class="visuallyhidden">Close</span>
  </span>
</button>


      <div class="modal-header">
        <h3 class="modal-title">
            
            Washington Post followed
        </h3>
      </div>

      <div class="modal-body">
        <div class="loading">
          <span class="spinner-bigger"></span>
        </div>
        <ol class="ScrollBumpDialog-usersList clearfix js-users-list"></ol>
      </div>
    </div>
  </div>
</div>





    <div id="timeline" class="ProfileTimeline ">
        <div class="stream-container  " data-max-position="1002549374394814465" data-min-position="1002526682924896258">
      <div class="stream-item js-new-items-bar-container new-tweets-bar-visible" style=""><button class="new-tweets-bar js-new-tweets-bar" data-item-count="1" style="width:100%">
        See 1 new Tweet

  </button></div>

    <div class="stream">
        <ol class="stream-items js-navigable-stream" id="stream-items-id">
          
      <li class="js-stream-item stream-item stream-item
" data-item-id="1002547612384362497" id="stream-item-tweet-1002547612384362497" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002547612384362497&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002547612384362497" data-item-id="1002547612384362497" data-permalink-path="/washingtonpost/status/1002547612384362497" data-conversation-id="1002547612384362497" data-tweet-nonce="1002547612384362497-2854746f-4556-4820-9cb5-6ca586e3bdbc" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002547612384362497" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:49 AM - 1 Jun 2018" data-conversation-id="1002547612384362497"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527860951" data-time-ms="1527860951000" data-long-form="true" aria-hidden="true">8m</span><span class="u-hiddenVisually" data-aria-label-part="last">8 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Washington’s answer to Vegas's Stanley Cup pregame festivities?
• Sting
• Shaggy
• Fall Out Boy
• Pat Sajak<a href="https://t.co/mwho7aJuvE" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2LfbSKx" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2LfbSKx"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2LfbSKx</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002547612384362497?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/mwho7aJuvE" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002547612384362497?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true" style="min-height: 362px;">
<iframe id="xdm_default4697_provider" style="display: block; margin: 0px; padding: 0px; border: 0px none;" scrolling="no" src="https://twitter.com/i/cards/tfw/v1/1002547612384362497?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en&amp;card_height=344&amp;scribe_context=%7B%22client%22%3A%22web%22%2C%22page%22%3A%22profile%22%2C%22section%22%3A%22profile%22%2C%22component%22%3A%22tweet%22%7D&amp;bearer_token=AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%252F40K4moUkGsoc%253DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw#xdm_e=https%3A%2F%2Ftwitter.com&amp;xdm_c=default4697&amp;xdm_p=1" allowfullscreen="" width="100%" height="362" frameborder="0"></iframe></div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="8">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002547612384362497" data-aria-label-part="">8 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="11">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002547612384362497" data-aria-label-part="">11 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="35">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002547612384362497" data-aria-label-part="">35 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002547612384362497">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">8</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002547612384362497">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">11</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">11</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002547612384362497">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">35</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">35</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002547076482453504" id="stream-item-tweet-1002547076482453504" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002547076482453504&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002547076482453504" data-item-id="1002547076482453504" data-permalink-path="/washingtonpost/status/1002547076482453504" data-conversation-id="1002547076482453504" data-tweet-nonce="1002547076482453504-29d682d5-09b0-41d1-a9ce-7dbd4ddea5c3" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002547076482453504" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:47 AM - 1 Jun 2018" data-conversation-id="1002547076482453504"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527860824" data-time-ms="1527860824000" data-long-form="true" aria-hidden="true">10m</span><span class="u-hiddenVisually" data-aria-label-part="last">10 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Facing reassignment under Trump, a well-regarded National Park Service official will instead retire<a href="https://t.co/FKik10Yccr" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2J0ZQYs" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2J0ZQYs"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2J0ZQYs</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002547076482453504?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/FKik10Yccr" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002547076482453504?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true" style="min-height: 362px;">
<iframe id="xdm_default4698_provider" style="display: block; margin: 0px; padding: 0px; border: 0px none;" scrolling="no" src="https://twitter.com/i/cards/tfw/v1/1002547076482453504?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en&amp;card_height=344&amp;scribe_context=%7B%22client%22%3A%22web%22%2C%22page%22%3A%22profile%22%2C%22section%22%3A%22profile%22%2C%22component%22%3A%22tweet%22%7D&amp;bearer_token=AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%252F40K4moUkGsoc%253DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw#xdm_e=https%3A%2F%2Ftwitter.com&amp;xdm_c=default4698&amp;xdm_p=1" allowfullscreen="" width="100%" height="362" frameborder="0"></iframe></div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="14">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002547076482453504" data-aria-label-part="">14 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="42">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002547076482453504" data-aria-label-part="">42 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="61">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002547076482453504" data-aria-label-part="">61 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002547076482453504">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">14</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002547076482453504">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">42</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">42</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002547076482453504">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">61</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">61</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002545618743676930" id="stream-item-tweet-1002545618743676930" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002545618743676930&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002545618743676930" data-item-id="1002545618743676930" data-permalink-path="/washingtonpost/status/1002545618743676930" data-conversation-id="1002545618743676930" data-tweet-nonce="1002545618743676930-6be31cd4-7fc3-4397-926f-b30da299ba04" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002545618743676930" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:41 AM - 1 Jun 2018" data-conversation-id="1002545618743676930"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527860476" data-time-ms="1527860476000" data-long-form="true" aria-hidden="true">16m</span><span class="u-hiddenVisually" data-aria-label-part="last">16 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">With its roots in wartime, National Doughnut Day is now just a caloric fun ride. Here’s where to get your freebies.<a href="https://t.co/QjIeRhznoo" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2LaNKZs" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2LaNKZs"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2LaNKZs</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002545618743676930?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/QjIeRhznoo" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002545618743676930?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="6">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002545618743676930" data-aria-label-part="">6 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="26">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002545618743676930" data-aria-label-part="">26 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="55">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002545618743676930" data-aria-label-part="">55 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002545618743676930">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">6</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002545618743676930">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">26</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">26</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002545618743676930">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">55</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">55</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002543436766044161" id="stream-item-tweet-1002543436766044161" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002543436766044161&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002543436766044161" data-item-id="1002543436766044161" data-permalink-path="/washingtonpost/status/1002543436766044161" data-conversation-id="1002543436766044161" data-tweet-nonce="1002543436766044161-b4cb2e1d-e74c-4c30-bfc5-f8a098fdc25d" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002543436766044161" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:32 AM - 1 Jun 2018" data-conversation-id="1002543436766044161"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527859956" data-time-ms="1527859956000" data-long-form="true" aria-hidden="true">25m</span><span class="u-hiddenVisually" data-aria-label-part="last">25 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Inside the fallout of America’s crackdown on opioids.

The race to end one crisis may be creating another — pain patients’ desperate search to secure medication.<a href="https://t.co/vBEFDhGsY9" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2HbsqRd" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2HbsqRd"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2HbsqRd</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002543436766044161?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/vBEFDhGsY9" data-publisher-id="87968068" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002543436766044161?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="7">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002543436766044161" data-aria-label-part="">7 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="37">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002543436766044161" data-aria-label-part="">37 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="54">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002543436766044161" data-aria-label-part="">54 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002543436766044161">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">7</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002543436766044161">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">37</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">37</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002543436766044161">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">54</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">54</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002541339291078663" id="stream-item-tweet-1002541339291078663" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002541339291078663&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002541339291078663" data-item-id="1002541339291078663" data-permalink-path="/washingtonpost/status/1002541339291078663" data-conversation-id="1002541339291078663" data-tweet-nonce="1002541339291078663-630c3e6b-57fd-415c-a481-58c6e0d393ba" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002541339291078663" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:24 AM - 1 Jun 2018" data-conversation-id="1002541339291078663"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527859456" data-time-ms="1527859456000" data-long-form="true" aria-hidden="true">33m</span><span class="u-hiddenVisually" data-aria-label-part="last">33 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Why the c-word is so taboo, and why some women want to reclaim it<a href="https://t.co/Ebcr8YaZSc" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2J3a5f4" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2J3a5f4"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2J3a5f4</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002541339291078663?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/Ebcr8YaZSc" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002541339291078663?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="119">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002541339291078663" data-aria-label-part="">119 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="57">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002541339291078663" data-aria-label-part="">57 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="148">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002541339291078663" data-aria-label-part="">148 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002541339291078663">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">119</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002541339291078663">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">57</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">57</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002541339291078663">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">148</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">148</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002540006186143744" id="stream-item-tweet-1002540006186143744" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002540006186143744&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002540006186143744" data-item-id="1002540006186143744" data-permalink-path="/washingtonpost/status/1002540006186143744" data-conversation-id="1002540006186143744" data-tweet-nonce="1002540006186143744-80179449-fb0f-41c6-95f3-99077c0fd10e" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002540006186143744" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:18 AM - 1 Jun 2018" data-conversation-id="1002540006186143744"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527859138" data-time-ms="1527859138000" data-long-form="true" aria-hidden="true">39m</span><span class="u-hiddenVisually" data-aria-label-part="last">39 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Analysis: Two major studies show election polls are not getting less accurate<a href="https://t.co/B4guPuqBo1" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2LdISTy" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2LdISTy"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2LdISTy</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002540006186143744?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/B4guPuqBo1" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002540006186143744?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="14">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002540006186143744" data-aria-label-part="">14 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="35">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002540006186143744" data-aria-label-part="">35 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="71">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002540006186143744" data-aria-label-part="">71 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002540006186143744">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">14</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002540006186143744">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">35</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">35</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002540006186143744">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">71</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">71</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002537601004396545" id="stream-item-tweet-1002537601004396545" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002537601004396545&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
       tweet-has-context
       has-cards cards-forward
" data-tweet-id="1002537601004396545" data-item-id="1002537601004396545" data-permalink-path="/newsbysamuels/status/1002537601004396545" data-conversation-id="1002537601004396545" data-tweet-nonce="1002537601004396545-e38d90b2-f8b7-446b-93ca-a2ea7e28426b" data-tweet-stat-initialized="true" data-retweet-id="1002539384187555840" data-retweeter="washingtonpost" data-screen-name="newsbysamuels" data-name="Robert Samuels" data-user-id="41210267" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;41210267&quot;,&quot;screen_name&quot;:&quot;newsbysamuels&quot;,&quot;name&quot;:&quot;Robert Samuels&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Robert Samuels&quot;,&quot;emojified_text_as_html&quot;:&quot;Robert Samuels&quot;}},{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
          <div class="tweet-context with-icn
    
    ">

      <span class="Icon Icon--small Icon--retweeted"></span>



            <span class="js-retweet-text">
                <a class="pretty-link js-user-profile-link" href="/washingtonpost" data-user-id="2467791" rel="noopener"><b>Washington Post</b></a> Retweeted
            </span>


      


    </div>

    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/newsbysamuels" data-user-id="41210267">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/443914661/s2401407_34811543_9979_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Robert Samuels</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>newsbysamuels</b></span></a>

        
        <small class="time">
  <a href="/newsbysamuels/status/1002537601004396545" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:09 AM - 1 Jun 2018" data-conversation-id="1002537601004396545"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527858564" data-time-ms="1527858564000" data-long-form="true" aria-hidden="true">48m</span><span class="u-hiddenVisually" data-aria-label-part="last">48 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>newsbysamuels</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>newsbysamuels</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>newsbysamuels</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>newsbysamuels</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">The first time I was called a monkey was in high school in NY. The 2nd time was at college in the Midwest. The third time, a Trump rally in the South. Roseanne's America, Trump's America is simply America. No place harbors sole ownership of its goodness:<a href="https://t.co/DSc6Pr8Isk" rel="nofollow noopener" dir="ltr" data-expanded-url="https://www.washingtonpost.com/news/post-nation/wp/2018/06/01/how-it-feels-to-be-called-a-monkey/?utm_term=.041c79bfc957" class="twitter-timeline-link u-hidden" target="_blank" title="https://www.washingtonpost.com/news/post-nation/wp/2018/06/01/how-it-feels-to-be-called-a-monkey/?utm_term=.041c79bfc957"><span class="tco-ellipsis"></span><span class="invisible">https://www.</span><span class="js-display-url">washingtonpost.com/news/post-nati</span><span class="invisible">on/wp/2018/06/01/how-it-feels-to-be-called-a-monkey/?utm_term=.041c79bfc957</span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span>…</span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002537601004396545?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/DSc6Pr8Isk" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002537601004396545?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="25">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002537601004396545" data-aria-label-part="">25 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="228">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002537601004396545" data-aria-label-part="">228 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="456">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002537601004396545" data-aria-label-part="">456 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002537601004396545">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">25</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002537601004396545">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">228</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">228</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002537601004396545">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">456</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">456</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002538698611789826" id="stream-item-tweet-1002538698611789826" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002538698611789826&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002538698611789826" data-item-id="1002538698611789826" data-permalink-path="/washingtonpost/status/1002538698611789826" data-conversation-id="1002538698611789826" data-tweet-nonce="1002538698611789826-9aac9fdd-3c17-4d26-9966-340be6dd34ed" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002538698611789826" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:13 AM - 1 Jun 2018" data-conversation-id="1002538698611789826"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527858826" data-time-ms="1527858826000" data-long-form="true" aria-hidden="true">44m</span><span class="u-hiddenVisually" data-aria-label-part="last">44 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">A dispute at school, a shooting later and one D.C. teen accused of killing another<a href="https://t.co/DfzCa2JJqt" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2H9Hy1E" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2H9Hy1E"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2H9Hy1E</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002538698611789826?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/DfzCa2JJqt" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002538698611789826?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="8">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002538698611789826" data-aria-label-part="">8 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="14">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002538698611789826" data-aria-label-part="">14 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="24">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002538698611789826" data-aria-label-part="">24 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002538698611789826">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">8</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002538698611789826">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">14</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">14</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002538698611789826">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">24</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">24</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002537356749139968" id="stream-item-tweet-1002537356749139968" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002537356749139968&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002537356749139968" data-item-id="1002537356749139968" data-permalink-path="/washingtonpost/status/1002537356749139968" data-conversation-id="1002537356749139968" data-tweet-nonce="1002537356749139968-138939cd-b9f0-4017-9264-de527451074c" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002537356749139968" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:08 AM - 1 Jun 2018" data-conversation-id="1002537356749139968"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527858506" data-time-ms="1527858506000" data-long-form="true" aria-hidden="true">49m</span><span class="u-hiddenVisually" data-aria-label-part="last">49 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">In a Georgia town, nine people explain their frustration and optimism on immigration<a href="https://t.co/hTS4BXh44C" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2J0Kgfn" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2J0Kgfn"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2J0Kgfn</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002537356749139968?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/hTS4BXh44C" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002537356749139968?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="8">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002537356749139968" data-aria-label-part="">8 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="13">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002537356749139968" data-aria-label-part="">13 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="29">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002537356749139968" data-aria-label-part="">29 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002537356749139968">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">8</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002537356749139968">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">13</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">13</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002537356749139968">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">29</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">29</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002535879427141632" id="stream-item-tweet-1002535879427141632" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002535879427141632&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002535879427141632" data-item-id="1002535879427141632" data-permalink-path="/washingtonpost/status/1002535879427141632" data-conversation-id="1002535879427141632" data-tweet-nonce="1002535879427141632-d8ed6cb8-5c6e-4c1f-bb7f-681cd6644c2c" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002535879427141632" class="tweet-timestamp js-permalink js-nav js-tooltip" title="9:02 AM - 1 Jun 2018" data-conversation-id="1002535879427141632"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527858154" data-time-ms="1527858154000" data-long-form="true" aria-hidden="true">55m</span><span class="u-hiddenVisually" data-aria-label-part="last">55 minutes ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">South Korea’s military just wants a golf course. But nothing is easy ahead of the Trump-Kim summit.<a href="https://t.co/WH304irb3J" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2LcFEjf" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2LcFEjf"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2LcFEjf</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002535879427141632?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/WH304irb3J" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002535879427141632?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="12">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002535879427141632" data-aria-label-part="">12 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="21">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002535879427141632" data-aria-label-part="">21 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="55">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002535879427141632" data-aria-label-part="">55 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002535879427141632">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">12</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002535879427141632">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">21</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">21</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002535879427141632">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">55</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">55</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002534442399920128" id="stream-item-tweet-1002534442399920128" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002534442399920128&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002534442399920128" data-item-id="1002534442399920128" data-permalink-path="/washingtonpost/status/1002534442399920128" data-conversation-id="1002534442399920128" data-tweet-nonce="1002534442399920128-0221965b-95e0-4f07-866a-a16cd9f7900f" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002534442399920128" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:56 AM - 1 Jun 2018" data-conversation-id="1002534442399920128"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527857811" data-time-ms="1527857811000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Thousands of South Carolinians won the lottery on Christmas — or so they thought. Now some are suing.<a href="https://t.co/IXJ44Mu52C" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2J3FI82" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2J3FI82"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2J3FI82</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002534442399920128?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/IXJ44Mu52C" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002534442399920128?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="2">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002534442399920128" data-aria-label-part="">2 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="17">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002534442399920128" data-aria-label-part="">17 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="36">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002534442399920128" data-aria-label-part="">36 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002534442399920128">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">2</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002534442399920128">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">17</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">17</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002534442399920128">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">36</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">36</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002533041263259649" id="stream-item-tweet-1002533041263259649" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002533041263259649&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002533041263259649" data-item-id="1002533041263259649" data-permalink-path="/washingtonpost/status/1002533041263259649" data-conversation-id="1002533041263259649" data-tweet-nonce="1002533041263259649-26c67b45-3ecb-4ba7-a866-d2c5b8dcb28c" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002533041263259649" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:51 AM - 1 Jun 2018" data-conversation-id="1002533041263259649"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527857477" data-time-ms="1527857477000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">U.S. economy continues its hiring spree and is projected to have added 200,000 jobs in May<a href="https://t.co/RY3WSkWaBX" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2J2EVVb" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2J2EVVb"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2J2EVVb</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002533041263259649?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/RY3WSkWaBX" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002533041263259649?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="26">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002533041263259649" data-aria-label-part="">26 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="19">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002533041263259649" data-aria-label-part="">19 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="59">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002533041263259649" data-aria-label-part="">59 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002533041263259649">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">26</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002533041263259649">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">19</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">19</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002533041263259649">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">59</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">59</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002532739021668352" id="stream-item-tweet-1002532739021668352" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002532739021668352&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002532739021668352" data-item-id="1002532739021668352" data-permalink-path="/washingtonpost/status/1002532739021668352" data-conversation-id="1002532739021668352" data-tweet-nonce="1002532739021668352-7b8fc383-4c84-4915-b12e-bb42c3c707a1" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002532739021668352" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:50 AM - 1 Jun 2018" data-conversation-id="1002532739021668352"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527857405" data-time-ms="1527857405000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Trump breaks with decades of protocol, hinting at positive jobs numbers before official release<a href="https://t.co/efbiwyD5lM" rel="nofollow noopener" dir="ltr" data-expanded-url="https://www.washingtonpost.com/news/business/wp/2018/06/01/trump-breaks-protocol-sends-markets-a-clear-signal-on-jobs-report-before-numbers-are-released/" class="twitter-timeline-link u-hidden" target="_blank" title="https://www.washingtonpost.com/news/business/wp/2018/06/01/trump-breaks-protocol-sends-markets-a-clear-signal-on-jobs-report-before-numbers-are-released/"><span class="tco-ellipsis"></span><span class="invisible">https://www.</span><span class="js-display-url">washingtonpost.com/news/business/</span><span class="invisible">wp/2018/06/01/trump-breaks-protocol-sends-markets-a-clear-signal-on-jobs-report-before-numbers-are-released/</span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span>…</span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002532739021668352?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/efbiwyD5lM" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002532739021668352?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="85">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002532739021668352" data-aria-label-part="">85 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="68">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002532739021668352" data-aria-label-part="">68 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="103">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002532739021668352" data-aria-label-part="">103 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002532739021668352">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">85</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002532739021668352">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">68</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">68</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002532739021668352">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">103</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">103</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002531635760377861" id="stream-item-tweet-1002531635760377861" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002531635760377861&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002531635760377861" data-item-id="1002531635760377861" data-permalink-path="/washingtonpost/status/1002531635760377861" data-conversation-id="1002531635760377861" data-tweet-nonce="1002531635760377861-b5d5b6c9-835b-494f-8e19-5a14cb028c96" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002531635760377861" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:45 AM - 1 Jun 2018" data-conversation-id="1002531635760377861"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527857142" data-time-ms="1527857142000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">New polls find most Americans say teachers are underpaid — and many would pay higher taxes to fix it<a href="https://t.co/rHacAPmPVM" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2J2qMaz" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2J2qMaz"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2J2qMaz</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002531635760377861?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/rHacAPmPVM" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002531635760377861?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="38">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002531635760377861" data-aria-label-part="">38 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="153">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002531635760377861" data-aria-label-part="">153 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="384">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002531635760377861" data-aria-label-part="">384 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002531635760377861">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">38</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002531635760377861">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">153</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">153</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002531635760377861">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">384</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">384</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002530253477236736" id="stream-item-tweet-1002530253477236736" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002530253477236736&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002530253477236736" data-item-id="1002530253477236736" data-permalink-path="/washingtonpost/status/1002530253477236736" data-conversation-id="1002530253477236736" data-tweet-nonce="1002530253477236736-0628c37b-cedd-4424-ac6c-23f31f4d52a5" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002530253477236736" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:40 AM - 1 Jun 2018" data-conversation-id="1002530253477236736"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527856813" data-time-ms="1527856813000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Trump says Samantha Bee has "no talent," asks why she hasn’t been fired<a href="https://t.co/2K3o2JxQU2" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2J1MMCd" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2J1MMCd"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2J1MMCd</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002530253477236736?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/2K3o2JxQU2" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002530253477236736?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="378">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002530253477236736" data-aria-label-part="">378 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="22">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002530253477236736" data-aria-label-part="">22 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="112">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002530253477236736" data-aria-label-part="">112 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002530253477236736">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">378</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002530253477236736">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">22</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">22</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002530253477236736">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">112</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">112</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002528717736996864" id="stream-item-tweet-1002528717736996864" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002528717736996864&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       
" data-tweet-id="1002528717736996864" data-item-id="1002528717736996864" data-permalink-path="/washingtonpost/status/1002528717736996864" data-conversation-id="1002528717736996864" data-tweet-nonce="1002528717736996864-26c117d5-4c7e-4e2d-9745-fe3f6eb75e25" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002528717736996864" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:34 AM - 1 Jun 2018" data-conversation-id="1002528717736996864"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527856447" data-time-ms="1527856447000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">The U.S. economy added 223,000 jobs in May, above expectations in a strong year for hiring <a href="https://t.co/O55dFERSLk" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2kGJ6r9" class="twitter-timeline-link" target="_blank" title="https://wapo.st/2kGJ6r9"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2kGJ6r9</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
      

      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="18">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002528717736996864" data-aria-label-part="">18 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="25">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002528717736996864" data-aria-label-part="">25 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="64">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002528717736996864" data-aria-label-part="">64 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002528717736996864">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">18</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002528717736996864">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">25</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">25</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002528717736996864">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">64</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">64</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002521592650452993" id="stream-item-tweet-1002521592650452993" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002521592650452993&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
       tweet-has-context
       has-cards cards-forward
" data-tweet-id="1002521592650452993" data-item-id="1002521592650452993" data-permalink-path="/wpjenna/status/1002521592650452993" data-conversation-id="1002521592650452993" data-tweet-nonce="1002521592650452993-7bdb233c-cb3a-4cb6-8e8d-d142aafbc12c" data-tweet-stat-initialized="true" data-retweet-id="1002528675164835840" data-retweeter="washingtonpost" data-screen-name="wpjenna" data-name="Jenna Johnson" data-user-id="15893354" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;15893354&quot;,&quot;screen_name&quot;:&quot;wpjenna&quot;,&quot;name&quot;:&quot;Jenna Johnson&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Jenna Johnson&quot;,&quot;emojified_text_as_html&quot;:&quot;Jenna Johnson&quot;}},{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
          <div class="tweet-context with-icn
    
    ">

      <span class="Icon Icon--small Icon--retweeted"></span>



            <span class="js-retweet-text">
                <a class="pretty-link js-user-profile-link" href="/washingtonpost" data-user-id="2467791" rel="noopener"><b>Washington Post</b></a> Retweeted
            </span>


      


    </div>

    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/wpjenna" data-user-id="15893354">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/735440046723993600/IQlKwH6p_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Jenna Johnson</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>wpjenna</b></span></a>

        
        <small class="time">
  <a href="/wpjenna/status/1002521592650452993" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:05 AM - 1 Jun 2018" data-conversation-id="1002521592650452993"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527854748" data-time-ms="1527854748000" data-long-form="true" aria-hidden="true">2h</span><span class="u-hiddenVisually" data-aria-label-part="last">2 hours ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>wpjenna</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>wpjenna</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>wpjenna</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>wpjenna</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">GOP candidates have been talking about immigration in all-caps tweets and ominous commercials — but in places like Gainesville, Ga., the discussion is often much more complicated, more immediate and more personal. Here are the views of nine locals...<a href="https://t.co/CkvBz8NEfo" rel="nofollow noopener" dir="ltr" data-expanded-url="https://www.washingtonpost.com/politics/in-a-georgia-town-10-people-explain-their-frustration-and-optimism-on-immigration/2018/05/30/820484a4-61b4-11e8-a69c-b944de66d9e7_story.html" class="twitter-timeline-link u-hidden" target="_blank" title="https://www.washingtonpost.com/politics/in-a-georgia-town-10-people-explain-their-frustration-and-optimism-on-immigration/2018/05/30/820484a4-61b4-11e8-a69c-b944de66d9e7_story.html"><span class="tco-ellipsis"></span><span class="invisible">https://www.</span><span class="js-display-url">washingtonpost.com/politics/in-a-</span><span class="invisible">georgia-town-10-people-explain-their-frustration-and-optimism-on-immigration/2018/05/30/820484a4-61b4-11e8-a69c-b944de66d9e7_story.html</span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span>…</span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002521592650452993?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/CkvBz8NEfo" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002521592650452993?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="3">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002521592650452993" data-aria-label-part="">3 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="45">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002521592650452993" data-aria-label-part="">45 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="82">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002521592650452993" data-aria-label-part="">82 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002521592650452993">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">3</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002521592650452993">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">45</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">45</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002521592650452993">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">82</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">82</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      
        <div class="self-thread-context">
  Show this thread
</div>


      
        <div class="self-thread-tweet-cta self-thread-head">
    <div class="mini-avatar-with-thread">
    <img class="avatar--circular size24" src="https://pbs.twimg.com/profile_images/735440046723993600/IQlKwH6p_normal.jpg">
  </div>

  <a href="/wpjenna/status/1002521592650452993" class="js-nav show-thread-link">Show this thread</a>
</div>


    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002528089749032971" id="stream-item-tweet-1002528089749032971" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002528089749032971&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002528089749032971" data-item-id="1002528089749032971" data-permalink-path="/washingtonpost/status/1002528089749032971" data-conversation-id="1002528089749032971" data-tweet-nonce="1002528089749032971-193c6bb9-df60-42e3-8d3c-803f510b69d4" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002528089749032971" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:31 AM - 1 Jun 2018" data-conversation-id="1002528089749032971"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527856297" data-time-ms="1527856297000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">Mueller’s investigation cost $16.7 million in just under a year, new documents show<a href="https://t.co/uoCFZ9dp4v" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2HaUJzc" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2HaUJzc"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2HaUJzc</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002528089749032971?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/uoCFZ9dp4v" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002528089749032971?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="124">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002528089749032971" data-aria-label-part="">124 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="20">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002528089749032971" data-aria-label-part="">20 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="70">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002528089749032971" data-aria-label-part="">70 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002528089749032971">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">124</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002528089749032971">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">20</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">20</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002528089749032971">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">70</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">70</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002528081272299520" id="stream-item-tweet-1002528081272299520" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002528081272299520&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002528081272299520" data-item-id="1002528081272299520" data-permalink-path="/washingtonpost/status/1002528081272299520" data-conversation-id="1002528081272299520" data-tweet-nonce="1002528081272299520-d42635bc-8e97-45e3-b528-6c06b93bdb49" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002528081272299520" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:31 AM - 1 Jun 2018" data-conversation-id="1002528081272299520"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527856295" data-time-ms="1527856295000" data-long-form="true" aria-hidden="true">1h</span><span class="u-hiddenVisually" data-aria-label-part="last">1 hour ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">D’Souza: In relaying pardon, Trump said he wants him to be "a bigger voice than ever"<a href="https://t.co/lbvfypP4qV" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2LawZxK" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2LawZxK"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2LawZxK</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002528081272299520?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/lbvfypP4qV" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002528081272299520?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="64">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002528081272299520" data-aria-label-part="">64 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="44">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002528081272299520" data-aria-label-part="">44 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="36">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002528081272299520" data-aria-label-part="">36 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002528081272299520">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">64</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002528081272299520">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">44</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">44</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002528081272299520">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">36</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">36</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="1002526682924896258" id="stream-item-tweet-1002526682924896258" data-item-type="tweet" data-suggestion-json="{&quot;suggestion_details&quot;:{},&quot;tweet_ids&quot;:&quot;1002526682924896258&quot;,&quot;scribe_component&quot;:&quot;tweet&quot;}" style="">
    


  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards cards-forward
" data-tweet-id="1002526682924896258" data-item-id="1002526682924896258" data-permalink-path="/washingtonpost/status/1002526682924896258" data-conversation-id="1002526682924896258" data-tweet-nonce="1002526682924896258-b1076bf5-12cd-4869-a288-9407a414ac8b" data-tweet-stat-initialized="true" data-screen-name="washingtonpost" data-name="Washington Post" data-user-id="2467791" data-you-follow="false" data-follows-you="false" data-you-block="false" data-reply-to-users-json="[{&quot;id_str&quot;:&quot;2467791&quot;,&quot;screen_name&quot;:&quot;washingtonpost&quot;,&quot;name&quot;:&quot;Washington Post&quot;,&quot;emojified_name&quot;:{&quot;text&quot;:&quot;Washington Post&quot;,&quot;emojified_text_as_html&quot;:&quot;Washington Post&quot;}}]" data-disclosure-type="" data-card2-type="summary_large_image" data-has-cards="true">

    <div class="context">
      
      
    </div>

    <div class="content">
      

      

      
      <div class="stream-item-header">
          <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/washingtonpost" data-user-id="2467791">
      <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/875440182501277696/n-Ic9nBO_bigger.jpg" alt="">
    <span class="FullNameGroup">
      <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">Washington Post</strong><span>‏</span><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>washingtonpost</b></span></a>

        
        <small class="time">
  <a href="/washingtonpost/status/1002526682924896258" class="tweet-timestamp js-permalink js-nav js-tooltip" title="8:26 AM - 1 Jun 2018" data-conversation-id="1002526682924896258"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1527855961" data-time-ms="1527855961000" data-long-form="true" aria-hidden="true">2h</span><span class="u-hiddenVisually" data-aria-label-part="last">2 hours ago</span></a>
</small>

          <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button" aria-haspopup="true">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--caretDownLight Icon--small"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu is-autoCentered">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
          <li class="mute-user-item"><button type="button" class="dropdown-link">Mute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>
    <li class="unmute-user-item"><button type="button" class="dropdown-link">Unmute <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button></li>

        <li class="block-link js-actionBlock" data-nav="block">
          <button type="button" class="dropdown-link">Block <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
        <li class="unblock-link js-actionUnblock" data-nav="unblock">
          <button type="button" class="dropdown-link">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>washingtonpost</b></span></button>
        </li>
      <li class="report-link js-actionReport" data-nav="report">
        <button type="button" class="dropdown-link">
          
            
            Report Tweet
        </button>
      </li>
      <li class="dropdown-divider"></li>
      <li class="js-actionMomentMakerAddTweetToOtherMoment MomentMakerAddTweetToOtherMoment">
        <button type="button" class="dropdown-link">Add to other Moment</button>
      </li>
      <li class="js-actionMomentMakerCreateMoment">
        <button type="button" class="dropdown-link">Add to new Moment</button>
      </li>
  </ul>
</div>

</div>

  </div>

      </div>

      

      


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" data-aria-label-part="0" lang="en">At Betsy DeVos’s federal school safety commission meeting, lessons from first-graders on friendships and fist bumps<a href="https://t.co/X4uuYxyxqR" rel="nofollow noopener" dir="ltr" data-expanded-url="https://wapo.st/2H9Jmrv" class="twitter-timeline-link u-hidden" target="_blank" title="https://wapo.st/2H9Jmrv"><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">wapo.st/2H9Jmrv</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a></p>
</div>


      

      
        


      
          <div class="card2 js-media-container
    " data-card2-name="summary_large_image">
    
<div class="js-macaw-cards-iframe-container initial-card-height card-type-summary_large_image" data-src="/i/cards/tfw/v1/1002526682924896258?cardname=summary_large_image&amp;autoplay_disabled=true&amp;forward=true&amp;earned=true&amp;edge=true&amp;lang=en" data-card-name="summary_large_image" data-card-url="https://t.co/X4uuYxyxqR" data-publisher-id="2467791" data-creator-id="" data-amplify-content-id="" data-amplify-playlist-url="" data-full-card-iframe-url="/i/cards/tfw/v1/1002526682924896258?cardname=summary_large_image&amp;autoplay_disabled=true&amp;earned=true&amp;edge=true&amp;lang=en" data-has-autoplayable-media="false" data-watched="true">
</div>

</div>



      
      <div class="stream-item-footer">
  
      <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="16">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-1002526682924896258" data-aria-label-part="">16 replies</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="16">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-retweet-count-aria-1002526682924896258" data-aria-label-part="">16 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount" data-tweet-stat-count="32">
        <span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-favorite-count-aria-1002526682924896258" data-aria-label-part="">32 likes</span>
      </span>
    </span>
  </div>

  <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
    <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-count-aria-1002526682924896258">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--medium Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <span class="ProfileTweet-actionCount ">
        <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">16</span>
      </span>
  </button>
</div>

    <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-retweet-count-aria-1002526682924896258">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">16</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--medium Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">16</span>
  </span>

  </button>
</div>


    <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-1002526682924896258">
    <div class="IconContainer js-tooltip" title="Like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">32</span>
  </span>

  </button><button class="ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <span role="presentation" class="Icon Icon--heart Icon--medium"></span>
      <div class="HeartAnimation"></div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <span class="ProfileTweet-actionCount">
    <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">32</span>
  </span>

  </button>
</div>


      <div class="ProfileTweet-action ProfileTweet-action--dm">
    <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionShareViaDM" type="button" data-nav="share_tweet_dm">
      <div class="IconContainer js-tooltip" title="Direct message">
        <span class="Icon Icon--medium Icon--dm"></span>
        <span class="u-hiddenVisually">Direct message</span>
      </div>
    </button>
  </div>


    

  </div>

</div>
  



      
      

      

      

    </div>

  </div>



    
<div class="dismiss-module">
  <div class="dismissed-module">
    <div class="feedback-actions">
        <div class="feedback-action" data-feedback-type="DontLike" data-feedback-url="">
          <div class="action-confirmation dismiss-module-item">Thanks. Twitter will use this to make your timeline better.
            <span class="undo-action">Undo</span>
          </div>
        </div>
    </div>
    <div class="child-feedback-confirmation">
      <div class="child-confirmation-item">
        <span class="child-confirmation-text"></span>
        <span class="undo-child-feedback-action">Undo</span>
      </div>
    </div>
  </div>
</div>

</li>















 

        </ol>
        <div class="stream-footer ">
  <div class="timeline-end has-items has-more-items">
      <div class="stream-end">
    <div class="stream-end-inner">
        <span class="Icon Icon--large Icon--logo"></span>

      <p class="empty-text">

          @washingtonpost hasn't Tweeted yet.
      </p>

        <p><button type="button" class="btn-link back-to-top hidden" style="display: inline-block;">Back to top ↑</button></p>
    </div>
  </div>


    <div class="stream-loading">
  <div class="stream-end-inner">
    <span class="spinner" title="Loading..."></span>
  </div>
</div>

  </div>
</div>
<div class="stream-fail-container">
    <div class="js-stream-whale-end stream-whale-end stream-placeholder centered-placeholder">
  <div class="stream-end-inner">
    <h2 class="title">Loading seems to be taking a while.</h2>
    <p>
      Twitter may be over capacity or experiencing a momentary hiccup. <a role="button" href="#" class="try-again-after-whale">Try again</a> or visit <a target="_blank" href="http://status.twitter.com" rel="noopener">Twitter Status</a> for more information.
    </p>
  </div>
</div>
</div>

      <ol class="hidden-replies-container"></ol>
    </div>
  </div>
    </div>


              </div>

                  <div class="Grid-cell u-size1of3">
                    <div class="Grid Grid--withGutter">
                      <div class="Grid-cell">
                        <div class="ProfileSidebar ProfileSidebar--withRightAlignment">
                          
                        <div class="MoveableModule">
                            
<div class="SidebarCommonModules">



        <div class="module wtf-module js-wtf-module roaming-module has-content">
  <div class="flex-module">
    <div class="flex-module-header">
      <h3>Who to follow</h3>
      <small>· </small>
      <button type="button" class="btn-link js-refresh-suggestions"><small>Refresh</small></button>
      <small class="view-all">· <a class="js-view-all-link js-nav" href="/who_to_follow/suggestions" data-element-term="view_all_link">View all</a></small>
    </div>

    <div class="js-recommended-followers dashboard-user-recommendations flex-module-inner" data-section-id="wtf" style="opacity: 1;"><div class="UserSmallListItem js-account-summary account-summary js-actionable-user" data-user-id="807095" data-feedback-token="131" data-impression-id="">
  <div class="UserSmallListItem-context">
  </div>

    <div class="dismiss js-action-dismiss"><span class="Icon Icon--close"></span></div>

  <div class="content">
    <a class="account-group js-recommend-link js-user-profile-link user-thumb" href="/nytimes" data-user-id="807095" rel="noopener">
      
      <img class="avatar js-action-profile-avatar " src="https://pbs.twimg.com/profile_images/942784892882112513/qV4xB0I3_bigger.jpg" alt="">
      <span class="account-group-inner" data-user-id="807095">
        <strong class="fullname">The New York Times</strong><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span><span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span>
      </span>
    </a>

        
<div class="user-actions not-following not-muting" data-screen-name="nytimes" data-user-id="807095">

  <span class="user-actions-follow-button js-follow-btn follow-button">
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    follow-text">
      <span aria-hidden="true">Follow</span>
      <span class="u-hiddenVisually">Follow <span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--primary
    EdgeButton--small 
    
    button-text
    following-text">
      <span aria-hidden="true">Following</span>
      <span class="u-hiddenVisually">Following <span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unfollow-text">
      <span aria-hidden="true">Unfollow</span>
      <span class="u-hiddenVisually">Unfollow <span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--invertedDanger
    EdgeButton--small 
    
    button-text
    blocked-text">
    <span aria-hidden="true">Blocked</span>
    <span class="u-hiddenVisually">Blocked <span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unblock-text">
    <span aria-hidden="true">Unblock</span>
    <span class="u-hiddenVisually">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    pending-text">
    <span aria-hidden="true">Pending</span>
    <span class="u-hiddenVisually">Pending follow request from <span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    cancel-text">
    <span aria-hidden="true">Cancel</span>
    <span class="u-hiddenVisually">Cancel your follow request to <span class="username u-dir u-textTruncate" dir="ltr">@<b>nytimes</b></span></span>
  </button>
</span>


</div>

  </div>
</div>

  
<div class="UserSmallListItem js-account-summary account-summary js-actionable-user" data-user-id="51241574" data-feedback-token="131" data-impression-id="">
  <div class="UserSmallListItem-context">
  </div>

    <div class="dismiss js-action-dismiss"><span class="Icon Icon--close"></span></div>

  <div class="content">
    <a class="account-group js-recommend-link js-user-profile-link user-thumb" href="/AP" data-user-id="51241574" rel="noopener">
      
      <img class="avatar js-action-profile-avatar " src="https://pbs.twimg.com/profile_images/461964160838803457/8z9FImcv_bigger.png" alt="">
      <span class="account-group-inner" data-user-id="51241574">
        <strong class="fullname">The Associated Press</strong><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span><span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span>
      </span>
    </a>

        
<div class="user-actions not-following not-muting" data-screen-name="AP" data-user-id="51241574">

  <span class="user-actions-follow-button js-follow-btn follow-button">
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    follow-text">
      <span aria-hidden="true">Follow</span>
      <span class="u-hiddenVisually">Follow <span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--primary
    EdgeButton--small 
    
    button-text
    following-text">
      <span aria-hidden="true">Following</span>
      <span class="u-hiddenVisually">Following <span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unfollow-text">
      <span aria-hidden="true">Unfollow</span>
      <span class="u-hiddenVisually">Unfollow <span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--invertedDanger
    EdgeButton--small 
    
    button-text
    blocked-text">
    <span aria-hidden="true">Blocked</span>
    <span class="u-hiddenVisually">Blocked <span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unblock-text">
    <span aria-hidden="true">Unblock</span>
    <span class="u-hiddenVisually">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    pending-text">
    <span aria-hidden="true">Pending</span>
    <span class="u-hiddenVisually">Pending follow request from <span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    cancel-text">
    <span aria-hidden="true">Cancel</span>
    <span class="u-hiddenVisually">Cancel your follow request to <span class="username u-dir u-textTruncate" dir="ltr">@<b>AP</b></span></span>
  </button>
</span>


</div>

  </div>
</div>

  
<div class="UserSmallListItem js-account-summary account-summary js-actionable-user" data-user-id="3108351" data-feedback-token="131" data-impression-id="">
  <div class="UserSmallListItem-context">
  </div>

    <div class="dismiss js-action-dismiss"><span class="Icon Icon--close"></span></div>

  <div class="content">
    <a class="account-group js-recommend-link js-user-profile-link user-thumb" href="/WSJ" data-user-id="3108351" rel="noopener">
      
      <img class="avatar js-action-profile-avatar " src="https://pbs.twimg.com/profile_images/971415515754266624/zCX0q9d5_bigger.jpg" alt="">
      <span class="account-group-inner" data-user-id="3108351">
        <strong class="fullname">The Wall Street Journal</strong><span class="UserBadges"><span class="Icon Icon--verified"><span class="u-hiddenVisually">Verified account</span></span></span><span class="UserNameBreak">&nbsp;</span><span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span>
      </span>
    </a>

        
<div class="user-actions not-following not-muting" data-screen-name="WSJ" data-user-id="3108351">

  <span class="user-actions-follow-button js-follow-btn follow-button">
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    follow-text">
      <span aria-hidden="true">Follow</span>
      <span class="u-hiddenVisually">Follow <span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--primary
    EdgeButton--small 
    
    button-text
    following-text">
      <span aria-hidden="true">Following</span>
      <span class="u-hiddenVisually">Following <span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unfollow-text">
      <span aria-hidden="true">Unfollow</span>
      <span class="u-hiddenVisually">Unfollow <span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--invertedDanger
    EdgeButton--small 
    
    button-text
    blocked-text">
    <span aria-hidden="true">Blocked</span>
    <span class="u-hiddenVisually">Blocked <span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--danger
    EdgeButton--small 
    
    button-text
    unblock-text">
    <span aria-hidden="true">Unblock</span>
    <span class="u-hiddenVisually">Unblock <span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    pending-text">
    <span aria-hidden="true">Pending</span>
    <span class="u-hiddenVisually">Pending follow request from <span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span></span>
  </button>
  <button type="button" class="
    EdgeButton
    EdgeButton--secondary
    EdgeButton--small 
    
    button-text
    cancel-text">
    <span aria-hidden="true">Cancel</span>
    <span class="u-hiddenVisually">Cancel your follow request to <span class="username u-dir u-textTruncate" dir="ltr">@<b>WSJ</b></span></span>
  </button>
</span>


</div>

  </div>
</div></div>
  </div>

      <div class="flex-module">
        <div class="flex-module-footer">
          <a href="/who_to_follow/import" class="js-find-friends-link js-nav" data-element-term="import_link">
            <span class="Icon Icon--small Icon--people"></span>Find people you know
          </a>
        </div>
      </div>

  
</div>


    <div class="module Trends trends">
  <div class="trends-inner"><div class="flex-module trends-container context-trends-container">
  <div class="flex-module-header">
    
    <h3><span class="trend-location js-trend-location">Trends for you</span></h3>
      <span class="middot" aria-hidden="true">·</span>
      <a role="button" href="#" data-modal="change-trends" class="btn-link change-trends js-trend-toggle">
        <span aria-hidden="true">Change</span>
        <span class="u-hiddenVisually">Change trend settings</span>
      </a>
  </div>
  <div class="flex-module-inner">
    <ul class="trend-items js-trends">
        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="#NationalDonutDay" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:hashtag_trend:taxi_country_source:tweet_count_10000_100000_metadescription:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex" href="/hashtag/NationalDonutDay?src=tren" data-query-source="trend_click" data-original-title="">
      <span class="u-linkComplex-target trend-name" dir="ltr">#NationalDonutDay</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          28.4K Tweets
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="#smwknd" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:hashtag_trend:taxi_country_source:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/hashtag/smwknd?src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">#smwknd</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="#JobsReport" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:hashtag_trend:taxi_country_source:tweet_count_1000_10000_metadescription:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/hashtag/JobsReport?src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">#JobsReport</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          6,471 Tweets
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="#BSIC18" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:hashtag_trend:taxi_country_source:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/hashtag/BSIC18?src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">#BSIC18</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="One Down" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:entity_trend:taxi_country_source:tweet_count_10000_100000_metadescription:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/search?q=%22One%20Down%22&amp;src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">One Down</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          81.9K Tweets
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="#WeAreStillIn" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:hashtag_trend:taxi_country_source:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/hashtag/WeAreStillIn?src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">#WeAreStillIn</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="Happy Pride Month" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:entity_trend:taxi_country_source:tweet_count_10000_100000_metadescription:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/search?q=%22Happy%20Pride%20Month%22&amp;src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">Happy Pride Month</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          50K Tweets
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="Niall Ferguson" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:entity_trend:taxi_country_source:tweet_count_1000_10000_metadescription:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/search?q=%22Niall%20Ferguson%22&amp;src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">Niall Ferguson</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          2,290 Tweets
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="#FridayFeeling" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:hashtag_trend:taxi_worldwide_source:tweet_count_10000_100000_metadescription:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/hashtag/FridayFeeling?src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">#FridayFeeling</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          66.5K Tweets
        </div>
    </a>

</li>

        <li class="trend-item js-trend-item  context-trend-item" data-trend-name="#ArchivesRoadTrip" data-trends-id="2288410772259088495" data-trend-token=":tailored_request:hashtag_trend:taxi_country_source:">

    <a class="pretty-link js-nav js-tooltip u-linkComplex " href="/hashtag/ArchivesRoadTrip?src=tren" data-query-source="trend_click">
      <span class="u-linkComplex-target trend-name" dir="ltr">#ArchivesRoadTrip</span>

      
      <div class="js-nav trend-item-context"></div>
        <div class="js-nav trend-item-stats">
          
        </div>
    </a>

</li>

    </ul>
  </div>
</div>
</div>
</div>


  <div class="Footer module roaming-module Footer--slim Footer--blankBackground">
  <div class="flex-module">
    <div class="flex-module-inner js-items-container">
      <ul class="u-cf">
        <li class="Footer-item Footer-copyright copyright">© 2018 Twitter</li>
        <li class="Footer-item"><a class="Footer-link" href="/about" rel="noopener">About</a></li>
        <li class="Footer-item"><a class="Footer-link" href="//support.twitter.com" rel="noopener">Help Center</a></li>
        <li class="Footer-item"><a class="Footer-link" href="/tos" rel="noopener">Terms</a></li>
        <li class="Footer-item"><a class="Footer-link" href="/privacy" rel="noopener">Privacy policy</a></li>
        <li class="Footer-item"><a class="Footer-link" href="//support.twitter.com/articles/20170514" rel="noopener">Cookies</a></li>
        <li class="Footer-item"><a class="Footer-link" href="//support.twitter.com/articles/20170451" rel="noopener">Ads info</a></li>
      </ul>
    </div>
  </div>

</div>

</div>

                          </div></div>
                      </div>
                    </div>
                  </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="trends_dialog" class="trends-dialog modal-container">
  <div class="modal draggable">
    <div class="modal-content">
      <button type="button" class="modal-btn modal-close js-close">
  <span class="Icon Icon--close Icon--medium">
    <span class="visuallyhidden">Close</span>
  </span>
</button>

      <div class="modal-header">
          <h3 class="modal-title">
            Trends
            
          </h3>
      </div>

      <div class="modal-body">

          <div class="trends-personalized content-placeholder" style="display: none;">
  <h2 class="title">Trends tailored just for you.</h2>
  <p>Trends offer a unique way to get closer to what you care about. They are tailored for you based on your location and who you follow.</p>
  <p class="placeholder-actions">
    <button type="button" class="EdgeButton EdgeButton--secondary customize-by-location">Change</button><button type="button" class="EdgeButton EdgeButton--primary done">Keep tailored trends</button>
  </p>
</div>


        <div class="trends-dialog-error">
          <p></p>
        </div>

        <div class="trends-wrapper" id="trends_dialog_content">
          
          <div class="loading">
            <span class="spinner-bigger"></span>
          </div>
        </div>
      </div>
        <div class="modal-footer trends-by-location" style="display: none;">
            <button type="button" class="EdgeButton EdgeButton--secondary select-default" data-personalized="true">Get tailored trends</button>
<button type="button" class="EdgeButton EdgeButton--primary done">Done</button>

        </div>
    </div>
  </div>
</div>


          </div>
"""

def test_following():
    profile = ParseProfile(PROFILE)
    assert profile.following_count == 1479

def test_followers():
    profile = ParseProfile(PROFILE)
    assert profile.follower_count == 12598791
    
def test_join_date():
    profile = ParseProfile(PROFILE)
    assert profile.join_date == datetime(2007, 3, 27, 7, 19)