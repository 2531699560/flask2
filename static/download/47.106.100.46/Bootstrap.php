<?php
class Bootstrap extends Yaf\Bootstrap_Abstract{
    public function _initCore(){
		ini_set('yaf.library', LIB_PATH);
		Yaf\Loader::import(CORE_PATH.'/Helper.php');
        Yaf\Loader::import(CORE_PATH.'/Basic.php');
		Yaf\Loader::import(CORE_PATH.'/BasicApps.php');
		Yaf\Loader::import(CORE_PATH.'/BasicAppsborrow.php');
		Yaf\Loader::import(CORE_PATH.'/BasicWeixin.php');
        Yaf\Loader::import(CORE_PATH.'/Model.php');
		Yaf\Loader::import(FUNC_PATH.'/F_Basic.php');
		Yaf\Loader::import(FUNC_PATH.'/F_Network.php');
		Yaf\Loader::import(FUNC_PATH.'/F_String.php');
		Yaf\Loader::import(FUNC_PATH.'/F_Validate.php');
    }

    public function _initRoute() {
        $router = Yaf\Dispatcher::getInstance()->getRouter();	
		
		//移动端投标-移动端
        $invest_mobile_detail = new Yaf\Route\Regex(
            '#mobile/borrow/buy/([0-9]+).html#',
            array('module' => 'mobile', 'controller' => 'borrow', 'action' => 'buy'),
            array(1 => 'id')
        );
        $router->addRoute('invest_mobile_detail', $invest_mobile_detail);			
        //标的明细-移动端
        $borrow_mobile_view = new Yaf\Route\Regex(
            '#mobile/borrow/view/([0-9]+).html#',
            array('module' => 'mobile', 'controller' => 'borrow', 'action' => 'view'),
            array(1 => 'id')
        );
        $router->addRoute('borrow_mobile_view', $borrow_mobile_view);	

        //投标结果明细-移动端
        $invest_mobile_view = new Yaf\Route\Regex(
            '#mobile/invest/detail/([0-9]+).html#',
            array('module' => 'mobile', 'controller' => 'invest', 'action' => 'detail'),
            array(1 => 'id')
        );
        $router->addRoute('invest_mobile_view', $invest_mobile_view);			
    }
	
    public function _initPlugin(Yaf\Dispatcher $dispatcher) {
        $router = new RouterPlugin();
        $dispatcher->registerPlugin($router);
		
        $user = new UserPlugin();
        $dispatcher->registerPlugin($user);
        Yaf\Registry::set('userPlugin', $user);
		
        $message = new MessagePlugin();
        $dispatcher->registerPlugin($message);
        Yaf\Registry::set('messagePlugin', $message);
		
        $sms = new SmsPlugin();
        $dispatcher->registerPlugin($sms);
        Yaf\Registry::set('smsPlugin', $sms);
    }
}